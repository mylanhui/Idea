# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
'''
外键 首单词小写，
'''
class User(models.Model):
    '''
    用户表
    1.身份标示
        0 学生
        1 教师
        2 团队
        3 管理员
    2.性别表示
        0 男
        1 女
    '''
    Id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=10, null=False, unique=True)
    Account = models.CharField(max_length=20, null=False, unique=True)
    PassWord = models.CharField(max_length=20, null=False)
    Identity = models.PositiveSmallIntegerField(default=0, null=False)
    Sex = models.PositiveSmallIntegerField(default=0, null=False)
    Email = models.EmailField(null=False, max_length=32, unique=True)
    Score = models.PositiveIntegerField(default=0, null=False)
    RegistTime = models.DateField(auto_now_add=True)
    Phone = models.CharField(max_length=12, null=False, )
    Img = models.ImageField(upload_to='photos/%Y/%m/%d/user', null=True)
    Introduction = models.TextField(null=True, max_length=200)
    School = models.CharField(null=True, max_length=20)
    Institude = models.CharField(null=True, max_length=20)
    Major = models.CharField(null=True, max_length=20)

    def __unicode__(self):
        return self.UserName


class Project(models.Model):
    '''
    项目表
    1.Status 项目状态描述
    '''
    Id = models.AutoField(primary_key=True)
    ProjectName = models.CharField(null=False, max_length=20, unique=True)
    Description = models.TextField(null=False, max_length=200)
    StartTime = models.DateField(auto_now_add=True)
    EndTime = models.DateField(null=False, )
    Statue = models.PositiveIntegerField(default=0)
    Number = models.PositiveIntegerField(default=1)
    Img = models.ImageField(upload_to='photos/%Y/%m/%d/project', null=True)
    Summary = models.TextField(null=True, max_length=200)
    Progress = models.TextField(null=True, max_length=200)

    def __unicode__(self):
        return self.ProjectName

class ProjectLabel(models.Model):
    '''
    项目标签表
    '''
    Id = models.AutoField(primary_key=True)
    ProjectLabelName = models.CharField(max_length=20, null=False, unique=True)
    IsUse = models.BooleanField(default=True)

class Project2ProjectLabel(models.Model):
    '''
    项目-项目标签表
    '''
    Id = models.AutoField(primary_key=True)
    projectLabel = models.ForeignKey(ProjectLabel, related_name='Project2ProjectLabel_ProjectLabel_set', null=False)
    project = models.ForeignKey(Project, related_name='Project2ProjectLabel_Project_set')


class UserLabel(models.Model):
    '''
    用户标签表
    '''
    Id = models.AutoField(primary_key=True)
    projectLabel = models.ForeignKey(Project, related_name='UserLabel_Project_set')
    IsUse = models.BooleanField(default=True)
    Name = models.CharField(null=False, max_length=20, unique=True)

class User2UserLabel(models.Model):
    '''
    用户-用户标签表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='User2UserLabel_User_set')
    userLabel = models.ForeignKey(UserLabel, related_name='User2UserLabel_UserLabel_set', null=False)


class ProjectUser(models.Model):
    '''
    项目-用户表
    1.项目身份状态
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='ProjectUser_User_set')
    project = models.ForeignKey(Project, related_name='ProjectUser_Project_set', null=False)
    Identity = models.PositiveIntegerField(default=0)
    Evaluate = models.TextField(max_length=200)

    def __unicode__(self):
        return self.project

class Creation(models.Model):
    '''
    创意表
    '''
    Id = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='Creation_User_set')
    projectlabel = models.ForeignKey(ProjectLabel, related_name='Creation_ProjectLabel_set', null=False)
    Describe = models.TextField(max_length=200, null=True)
    Name = models.CharField(max_length=20, null=False)
    IsUse = models.BooleanField(default=True)
    Img = models.ImageField(upload_to='photos/%Y/%m/%d/creation')

    def __unicode__(self):
        return self.Name

class Creation2ProjectLabel(models.Model):
    Id = models.AutoField(primary_key=True)
    creation = models.ForeignKey(Creation,related_name='Creation2ProjectLabel_Creation_set', null=False)
    projectLabel = models.ForeignKey(ProjectLabel, related_name='Creation2ProjectLabel_ProjectLabel_set', null=False)

    def __unicode__(self):
        return self.creation


class Recruit(models.Model):
    '''
    招募表
    '''
    Id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, related_name='Recruit_Project_set', null=False)
    StartTime = models.DateField(auto_now_add=True)
    EndTime = models.DateField(null=True)
    Describe = models.TextField(null=False, max_length=200)
    State = models.PositiveIntegerField(default=0)
    Times = models.PositiveIntegerField(default=1)
    PredictNuber = models.PositiveIntegerField(default=1)
    RecruitedNuber = models.PositiveIntegerField(default=0)

class Praise(models.Model):
    '''
    赞扬表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Praise_User_set', null=True)
    creation = models.ForeignKey(Creation, related_name='Praise_Creation_set', null=True)
    project = models.ForeignKey(Project, related_name='Praise_Project_set', null=True)

    def __unicode__(self):
        return self.Id

class Apply(models.Model):
    '''
    申请表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Apply_User_set', null=False)
    recruit = models.ForeignKey(Recruit, related_name='Apply_Recruit_set', null=False)
    Describe = models.TextField(null=True, max_length=200)
    State = models.PositiveIntegerField(default=0)
    SendTime = models.DateField(auto_now_add=True)

class Message(models.Model):
    '''
    消息表
    1.优先级（默认为0）
    2.消息类型（默认为0）
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Message_User_set', null=False)
    Priority = models.PositiveIntegerField(default=0)
    Type = models.PositiveIntegerField(default=0)
    Date = models.DateField(auto_now_add=True)
    IsRead = models.BooleanField(default=False)
    Content = models.TextField(max_length=200, null=False)

class Comment(models.Model):
    '''
    评论表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Comment_User_set', null=False)
    creation = models.ForeignKey(Creation, related_name='Comment_Creation_set', null=True)
    project = models.ForeignKey(Project, related_name='Comment_Project_set', null=True)
    Date = models.DateField(auto_now_add=True)
    Content = models.TextField(max_length=200)
    IsUse = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user

class Follow(models.Model):
    '''
    关注表
    '''
    Id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, related_name='Follow_Project_set', null=True)
    creation = models.ForeignKey(Creation, related_name='Follow_Creation_set', null=True)
    user = models.ForeignKey(User, related_name='Follow_User_set', null=False)
    Follower = models.ForeignKey(User, related_name='Follow_Follower_set', null=False)

    def __unicode__(self):
        return self.user
class Report(models.Model):
    '''
    举报表
    1.处理状态，默认为0
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Report_User_set', null=False)
    project = models.ForeignKey(Project, related_name='Report_Project_set', null=True)
    creation = models.ForeignKey(Creation, related_name='Report_Creation_set', null=True)
    comment = models.ForeignKey(Comment, related_name='Report_Comment_set', null=True)
    Reason = models.TextField(max_length=200)
    ReportDate = models.DateField(auto_now_add=True)
    DealTime = models.DateField(null=True)
    State = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.comment

class Score(models.Model):
    '''
    分值等级表
    1.分值等级，默认为0
    '''
    Id = models.AutoField(primary_key=True)
    Level = models.PositiveIntegerField(default=0)
    Value = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return self.Level

class ScoreChange(models.Model):
    '''
    分值变动记录表

    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='ScoreChange_User_set', null=False)
    score = models.ForeignKey(Score, related_name='ScoreChange_Score_set', null=False)
    Event = models.CharField(null=True,max_length=30)
    Date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.user
'''
将数据库字段注册到Django自带后台，方便数据添加测试
后台账号为admin 密码adminadmin
'''
admin.site.register(User)
admin.site.register(UserLabel)
admin.site.register(User2UserLabel)
admin.site.register(Project)
admin.site.register(ProjectLabel)
admin.site.register(Project2ProjectLabel)
admin.site.register(ProjectUser)
admin.site.register(Creation)
admin.site.register(Recruit)
admin.site.register(Praise)
admin.site.register(Apply)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Report)
admin.site.register(Score)
admin.site.register(ScoreChange)
admin.site.register(Creation2ProjectLabel)
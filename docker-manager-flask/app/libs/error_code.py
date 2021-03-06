""" 
@Time    : 2018/7/18 19:21
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : error_code.py
@Desc    :
"""

from app.libs.error import APIException

class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0

class DeleteSuccess(Success):
    code = 202
    error_code = 1
    msg = 'delete success'

class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006

class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001

class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005

class Forbidden(APIException):
    code = 403
    msg = 'forbidden,not in scope'
    error_code = 1004

class ModifyFailed(APIException):
    code = 401
    msg = 'Unequal data'
    error_code = 1009

class RepeatFailed(APIException):
    code = 401
    msg = 'data is exist,cannot repeat'
    error_code = 1010

class ImageNotFound(APIException):
    code = 500
    msg = '无此镜像，请刷新重试'
    error_code = 1016

class FileTypeError(APIException):
    code = 401
    msg = 'file type is error'
    error_code = 1017

class ImageUsed(APIException):
    code = 500
    msg = '镜像已被使用请删除容器后重试'
    error_code = 1018

class DockerRunFail(APIException):
    code = 500
    msg = '容器运行失败，请检查参数后重试'
    error_code = 1020

class PullFail(APIException):
    code = 500
    msg = '拉取镜像失败，请检查tag后重试'
    error_code = 1021

class StopFail(APIException):
    code = 500
    msg = '容器停止失败，请刷新后重试'
    error_code = 1022

class StartFail(APIException):
    code = 500
    msg = '容器启动失败，请刷新后重试'
    error_code = 1023

class RemoveFail(APIException):
    code = 500
    msg = '容器删除失败，请刷新后重试'
    error_code = 1024
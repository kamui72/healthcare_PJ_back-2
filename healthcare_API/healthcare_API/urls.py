"""
URL configuration for healthcare_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ゲストユーザーのダッシュボードを表示するビュー
    path('guest-dashboard/', views.guest_dashboard, name='guest_dashboard'),

    # ゲストユーザーから登録ユーザーへの昇格処理
    path('upgrade-guest/', views.upgrade_guest_to_user, name='upgrade_guest'),
]

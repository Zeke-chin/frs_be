NAME=frs_be
VERSION=latest
BUILD_TIME      := $(shell date "+%F %T")
COMMIT_SHA1     := $(shell git rev-parse HEAD)
AUTHOR          := $(shell git show -s --format='%an')


.PHONY: all dev pro

dev:
	@docker build -t registry.cn-hangzhou.aliyuncs.com/zekechin/$(NAME):latest --build-arg FLASK_ENV='development' .
	@docker push registry.cn-hangzhou.aliyuncs.com/zekechin/$(NAME):latest

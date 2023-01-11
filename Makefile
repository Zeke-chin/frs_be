NAME=meta_admin
VERSION=latest
BUILD_TIME      := $(shell date "+%F %T")
COMMIT_SHA1     := $(shell git rev-parse HEAD)
AUTHOR          := $(shell git show -s --format='%an')


.PHONY: all dev pro

dev:
	@docker build -t SXKJ:32775/meta_$(NAME):latest --build-arg FLASK_ENV='development' .
	@docker push SXKJ:32775/meta_$(NAME):latest

pro:
	@docker build -t registry-vpc.cn-hangzhou.aliyuncs.com/sxkj/meta_$(NAME):latest --build-arg FLASK_ENV='production' .
	@docker push registry-vpc.cn-hangzhou.aliyuncs.com/sxkj/meta_$(NAME):latest

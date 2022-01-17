# Lab 32: Django permissions and docker with postgres

The purpose of this lab assignment is to become more familiar with building from the beginning a docker project again (same as yesterdays assignment), except with user permissions added and using postgres instead of sqllite. Docker is still being used.

Second part of this lab is to add authentication (using restframeworksimplejwt) and to switch from using django's runserver to a more production appropriate server, gunicorn. Switching to gunicorn causes issues with static files, and those are now connected with whitenoise along with compression and caching.

## Link to pull request:

- [PR #1 on 1/13/21](https://github.com/chloenott/drf-api-permissions-postgres/pull/1)

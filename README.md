# League Advisor API

### We are deployed on *GitHub*

[League Advisor API](https://github.com/League-Advisor/league-advisor-api)

---

## API Server

[League Advisor API Server!](https://league-advisor-api--v1.herokuapp.com)

---

## Features and Tests

### *TBA*

---

## User Stories

[User Stories](https://github.com/orgs/League-Advisor/projects/2)

---

## Domain Model

![Domain Model](assets/Domain_Model.png)

- Items marked with * are stretch goals or may require different approach.

---

## Database Schema Diagram

![Database Schema](assets/Database_Schema.png)

- Items marked with * are stretch goals or may require different approach.

---

## Project Directory Tree

### *TBA*

---

## Tools Used

[GitHub Projects - League Advisor Web App](https://github.com/orgs/League-Advisor/projects/2)

- Python
- Poetry
- Django
- restframework
- Django-rest-framework
- Django-cors-headers
- pytz
- PyJWT
- DateTime
- bs4
- requests
- pandas
- cdifflib
- collections-extended
- django-nose
- coverage

---

## Getting Started

### *TBA*

---

## Change Log

v0.1: _feat: started project and created project repo_ - 08 Dec 2021

v0.1.1 _docs: added requirements, domain model and db schema_ - 08 Dec 2021

v0.1.2 _docs: edited domain model and db schema_ - 09 Dec 2021

v0.1.3 _feat: create django project and account app_ - 09 Dec 2021

v0.1.4 _feat: create account model_ - 10 Dec 2021

v0.2.0 _feat: created champions app_ - 10 Dec 2021

v0.2.1 _tests: added champions app tests_ - 10 Dec 2021

v0.2.3 _feat: created patch_notes app_ - 10 Dec 2021

v0.2.4 _tests: added patch_notes app tests_ - 10 Dec 2021

v0.2.5 _feat: modified champions command to include stretch goals_ - 11 Dec 2021

v0.1.5 _feat: create account register, login, logout and, user (views & serializers)_ - 10 Dec 2021

v0.1.6 _feat: fill out the account-model fields with riot-games-datasets_ - 11 Dec 2021

v0.1.7 _refactor: accounts-app api data refactor and adding env variables_ - 12 Dec 2021

v0.1.8 _fix: avoid errors on invalid summonername_ - 12 Dec 2021

v0.1.9 test:_ading account test file and test (views, model)_ - 12 Dec 2021

v0.2.6 _feat: automated detecting newer patch release and updating data_ - 11 Dec 2021

v0.2 _feat: create items app and some tests_ - 10 Dec 2021

v0.4.0 :_feat: created solo champion app and ranked app_ - 11 Dec 2021

v0.4.1 :_feat: refacring ranked app_ - 11 Dec 2021

v0.4.2 :_test: adding tests for solo champion_ - 12 Dec 2021

v0.4.3 :_test: make a test for ranked app_ - 12 Dec 2021

v0.5.0 :_refactor: automate populating items_ - 12 Dec 2021

v0.5.1 :_refactor: initial db population and automating version reading_ - 12 Dec 2021

v0.5.3 :_test: update tests_ - 12 Dec 2021

v0.5.4 :_fix: added temporary alternative login/registration method_ - 13 Dec 2021

v0.5.5 :_fix: adjusted temporary alternative login/registration method returned data_ - 13 Dec 2021

v0.5.6 :_fix: stroing hashed normal user password_ - 13 Dec 2021

v0.5.7 :_fix: fixed static assets_ - 13 Dec 2021

v0.5.8 :_feat: added summoner profile update feature_ - 14 Dec 2021

v0.5.9 :_fix: summoner profile update non auth_ - 15 Dec 2021

v0.6.0 :_fix: refined code_ - 15 Dec 2021

v0.6.1 :_test: test ranked app_ - 15 Dec 2021

v0.6.2 :_test: refactor accounts tests_ - 15 Dec 2021

v0.6.3 :_tests: testing champions app_ - 15 Dec 2021

v0.6.4 :_test: test ranked app_ - 15 Dec 2021

v0.6.5 :_test: solo champion_ - 15 Dec 2021

v0.6.4 :_test: edit ranked test_ - 15 Dec 2021

v0.6.6 :_create: create docker container_ -15 Dec 2021

v0.6.7 :_deploy: deploy league-advisor-api-v1_ -15 Dec 2021

v0.6.8 :_docs: added test coverage and api server_ -16 Dec 2021

---

## Test Coverage

```py
Name                                                   Stmts   Miss  Cover
--------------------------------------------------------------------------
accounts/__init__.py                                       0      0   100%
accounts/admin.py                                          7      0   100%
accounts/apps.py                                           4      0   100%
accounts/migrations/0001_initial.py                        8      0   100%
accounts/migrations/__init__.py                            0      0   100%
accounts/models.py                                        58      4    93%
accounts/serializers.py                                   27      6    78%
accounts/urls.py                                           3      0   100%
accounts/views.py                                         54     34    37%
champions/__init__.py                                      1      0   100%
champions/admin.py                                         3      0   100%
champions/apps.py                                         18      7    61%
champions/management/__init__.py                           0      0   100%
champions/management/commands/__init__.py                  0      0   100%
champions/management/commands/populate_champions.py       28     21    25%
champions/migrations/0001_initial.py                       6      0   100%
champions/migrations/0002_remove_champion_creator.py       4      0   100%
champions/migrations/__init__.py                           0      0   100%
champions/models.py                                       20      1    95%
champions/serializers.py                                   6      0   100%
champions/urls.py                                          3      0   100%
champions/views.py                                         9      0   100%
items/__init__.py                                          0      0   100%
items/admin.py                                             3      0   100%
items/apps.py                                              4      0   100%
items/management/commands/items.py                        18     10    44%
items/migrations/0001_initial.py                           5      0   100%
items/migrations/__init__.py                               0      0   100%
items/models.py                                           11      1    91%
items/serializers.py                                       6      0   100%
items/urls.py                                              3      0   100%
items/views.py                                            10      0   100%
patch_notes/__init__.py                                    0      0   100%
patch_notes/admin.py                                       1      0   100%
patch_notes/apps.py                                        4      0   100%
patch_notes/urls.py                                        3      0   100%
patch_notes/views.py                                      15      0   100%
ranked/__init__.py                                         0      0   100%
ranked/admin.py                                            1      0   100%
ranked/apps.py                                             4      0   100%
ranked/models.py                                           0      0   100%
ranked/urls.py                                             3      0   100%
ranked/views.py                                          130      2    98%
solo_champion/__init__.py                                  0      0   100%
solo_champion/admin.py                                     1      0   100%
solo_champion/apps.py                                      4      0   100%
solo_champion/models.py                                    1      0   100%
solo_champion/urls.py                                      3      0   100%
solo_champion/views.py                                    27      0   100%
--------------------------------------------------------------------------
TOTAL                                                    516     86    83%
----------------------------------------------------------------------
```
---

## Authors

- Bashar Taamneh
- Du'a Jaradat
- Ehab Ahmad
- Mohammed Al-Hanbali

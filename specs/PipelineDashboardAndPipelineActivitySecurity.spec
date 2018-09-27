Copyright 2018 ThoughtWorks, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

PipelineDashboardAndPipelineActivitySecurity
============================================

Setup of contexts
* Permissions configuration - setup
* Login as "admin" - setup
* Using pipeline "P1, P2, P3, P4" - setup
* With "2" live agents - setup
* Capture go state "PipelineDashboardAndPipelineActivitySecurity" - setup

PipelineDashboardAndPipelineActivitySecurity
--------------------------------------------

tags: 6786, Permissions, long_running

Verify that super-admin has all view and operate permissions

* Looking at pipeline "P1" - On Swift Dashboard page
* Trigger and wait for stage "defaultStage" is "Passed" with label "1" - On Swift Dashboard page
* Looking at pipeline "P2" - On Swift Dashboard page
* Trigger and wait for stage "defaultStage" is "Passed" with label "1" - On Swift Dashboard page
* Looking at pipeline "P3" - On Swift Dashboard page
* Trigger and wait for stage "defaultStage" is "Passed" with label "1" - On Swift Dashboard page
* Looking at pipeline "P4" - On Swift Dashboard page
* Trigger and wait for stage "defaultStage" is "Passed" with label "1" - On Swift Dashboard page


Pipeline Visibility
* PipelineVisibility 
     |Pipeline Name|Visible?|Can Operate Using Ui?|Can Pause Using Api?|Can Pause Using Ui?|Can Operate Using API?|
     |-------------|--------|---------------------|--------------------|-------------------|----------------------|
     |P1           |true    |true                 |true                |true               |true                  |
     |P2           |true    |true                 |true                |true               |true                  |
     |P3           |true    |true                 |true                |true               |true                  |
     |P4           |true    |true                 |true                |true               |true                  |


* verify user has operate permissions on "defaultStage" for pipeline "P1" on Pipeline Activity Page
* Verify pipeline with label "1" is triggered by "admin"

* verify user has operate permissions on "defaultStage" for pipeline "P2" on Pipeline Activity Page

* verify user has operate permissions on "defaultStage" for pipeline "P3" on Pipeline Activity Page

* verify user has operate permissions on "defaultStage" for pipeline "P4" on Pipeline Activity Page


* Logout - from any page

* Login as "raghu"


Pipeline Visibility
* PipelineVisibility 
     |Pipeline Name|Visible?|Can Operate Using Ui?|Can Pause Using Api?|Can Pause Using Ui?|Can Operate Using API?|
     |-------------|--------|---------------------|--------------------|-------------------|----------------------|
     |P1           |true    |false                |false               |false              |false                 |
     |P2           |true    |true                 |true                |true               |true                  |
     |P3           |true    |true                 |true                |true               |true                  |
     |P4           |false   |false                |true                |false              |true                  |



* verify user does not have operate permissions on "defaultStage" for pipleine "P1" on pipeline activity page
* verify user has operate permissions on "defaultStage" for pipeline "P2" on Pipeline Activity Page
* verify user has operate permissions on "defaultStage" for pipeline "P3" on Pipeline Activity Page


* Logout - from any page

* Login as "pavan"


Pipeline Visibility
* PipelineVisibility 
     |Pipeline Name|Visible?|Can Operate Using Ui?|Can Pause Using Api?|Can Pause Using Ui?|Can Operate Using API?|
     |-------------|--------|---------------------|--------------------|-------------------|----------------------|
     |P1           |true    |false                |false               |false              |false                 |
     |P2           |false   |false                |false               |false              |false                 |
     |P3           |true    |true                 |true                |true               |true                  |
     |P4           |false   |false                |false               |false              |false                 |



* verify user does not have operate permissions on "defaultStage" for pipleine "P1" on pipeline activity page
* verify user has operate permissions on "defaultStage" for pipeline "P3" on Pipeline Activity Page


* Logout - from any page

* Login as "group1View"


Pipeline Visibility
* PipelineVisibility 
     |Pipeline Name|Visible?|Can Operate Using Ui?|Can Pause Using Api?|Can Pause Using Ui?|Can Operate Using API?|
     |-------------|--------|---------------------|--------------------|-------------------|----------------------|
     |P1           |false   |false                |true                |false              |true                  |
     |P2           |true    |true                 |true                |true               |true                  |
     |P3           |true    |false                |true                |true               |false                 |
     |P4           |true    |false                |false               |false              |false                 |




* verify user has operate permissions on "defaultStage" for pipeline "P2" on Pipeline Activity Page
* verify user does not have operate permissions on "defaultStage" for pipleine "P4" on pipeline activity page
* verify user does not have stage "defaultStage" operate permissions for pipleine "P3" on pipeline activity page

Teardown of contexts
____________________
* Capture go state "PipelineDashboardAndPipelineActivitySecurity" - teardown
* With "2" live agents - teardown



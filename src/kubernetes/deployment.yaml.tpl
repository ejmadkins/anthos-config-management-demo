# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: apps/v1
kind: Deployment
metadata:
  name: t-rex-app
  namespace: t-rex-app
  labels:
    app: t-rex-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: t-rex-app
  template:
    metadata:
      labels:
        app: t-rex-app
      annotations:
#        alpha.image-policy.k8s.io/break-glass: "true"
    spec:
      containers:
      - name: t-rex-app
        image: gcr.io/GOOGLE_CLOUD_PROJECT/t-rex-app@DIGEST
        ports:
        - containerPort: 8080
        resources:
          limits:
            cpu: "100m"
            memory: "1Gi"
        securityContext:
          runAsUser: 2000
          allowPrivilegeEscalation: false
          privileged: false
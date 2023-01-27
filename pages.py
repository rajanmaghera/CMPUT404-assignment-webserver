
# Copyright 2023 Rajan Maghera
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''This module contains the pages that are sent to the client.'''

PAGE404 = """<html>
<head>
<title>404 Not Found</title>
</head>
<body>
<h1>404 Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body>
</html>
"""

PAGE405 = """<html>
<head>
<title>405 Method Not Allowed</title>
</head>
<body>
<h1>405 Method Not Allowed</h1>
<p>The requested method is not allowed on this server.</p>
</body>
</html>
"""

PAGE400 = """<html>
<head>
<title>400 Bad Request</title>
</head>
<body>
<h1>400 Bad Request</h1>
<p>The request could not be processed due to it being incorrect.</p>
</body>
</html>
"""
# Copyright 2020 Google LLC
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

from typing import Dict, Optional
from setup_gmail import Message

class MessageDao(object):
    def __init__(self):
        # Maps message.id to message
        self._messages_seen : Dict[str, Message] = {}

    def store(self, message : Message):
        self._messages_seen[message.id] = message

    def get(self, message_id : str) -> Optional[Message]:
        return self._messages_seen.get(message_id)

    def size(self) -> int:
        return len(self._messages_seen)
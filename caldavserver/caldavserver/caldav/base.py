# Copyright (C) 2022 Code for Vegas Foundation
# 
# This file is part of be-smart-calendar-server-py.
# 
# be-smart-calendar-server-py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# be-smart-calendar-server-py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with be-smart-calendar-server-py.  If not, see <http://www.gnu.org/licenses/>.

import logging
logger = logging.getLogger(__name__)

class BaseCalDAVHandler(object):

	state = dict(request=None)

	def __init__(self, req=None):
		if req:
			self.parse_request(req)

	def run(self):
		logger.debug(f"{self.__class__.__name__}.run")
		return self

	def status(self, item=None):
		if item:
			return self.state.get(item)
		return self.state

	def parse_request(self, req=None):
		if req is None:
			self.state['request'] = None
		return self

	def parse_path(self):
		return self

	def check_authorization(self):
		return self


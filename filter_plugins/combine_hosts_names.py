#!/usr/bin/env python

from __future__ import absolute_import
import linchpin.FilterUtils.FilterUtils as filter_utils


class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'combine_hosts_names': filter_utils.combine_hosts_names
        }

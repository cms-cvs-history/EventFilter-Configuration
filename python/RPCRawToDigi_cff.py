import FWCore.ParameterSet.Config as cms

import copy
from HLTrigger.HLTcore.hltPrescaler_cfi import *
#
# David Lange, LLNL
# February 26, 2007
#
# Definition of RPCRawToDigi sequence
#
#to be true raw to digi sequence -- meanwhile prescaler placeholder
rpcRTDPlaceholder = copy.deepcopy(hltPrescaler)
from EventFilter.Configuration.DigiToRaw_cff import *
RPCRawToDigi = cms.Sequence(DigiToRaw*rpcRTDPlaceholder)
rpcRTDPlaceholder.prescaleFactor = 1


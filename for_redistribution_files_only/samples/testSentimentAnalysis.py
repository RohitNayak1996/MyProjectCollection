#!/usr/bin/env python
"""
Sample script that uses the sentimentAnalysisVADER module created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""

from __future__ import print_function
import sentimentAnalysisVADER
import matlab

my_sentimentAnalysisVADER = sentimentAnalysisVADER.initialize()

inputTextIn = "This is adequate test input for our sentiment analysis code"
sentimentOut, scoresOut = my_sentimentAnalysisVADER.sentimentAnalysisVADER(inputTextIn, nargout=2)
print(sentimentOut, scoresOut, sep='\n')

my_sentimentAnalysisVADER.terminate()

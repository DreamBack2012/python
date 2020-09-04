#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   anyfile2pdf.py
#@Time    :   2020/09/04 16:09:36
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

from win32com.client import gencache
from win32com.client import constants, gencache

class AnyFile2PDF():
    """将任何格式的文件转为pdf"""

    def word2pdf(self, wordPath, pdfPath):
        """
        word转pdf
        :param wordPath: word文件路径
        :param pdfPath:  生成pdf文件路径
        """
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(wordPath, ReadOnly=1)
        doc.ExportAsFixedFormat(pdfPath,
                                constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        word.Quit(constants.wdDoNotSaveChanges)

if __name__ == "__main__":
    convert = AnyFile2PDF()
    convert.word2pdf("E:/work/file/转码失败/水印.docx", "E:/work/file/转码失败/水印.pdf")

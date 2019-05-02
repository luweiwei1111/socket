import logging
import logging.config

logging.config.fileConfig("conf/logger.conf")

# 输出日志到控制台,获取的是root对应的logger
console_logger = logging.getLogger()
 
# 输出日志到单个文件
file_logger = logging.getLogger(name="fileLogger")
 
# rotatingFileLogger中，consoleHandler输出到控制台，rotatingHandler输出日志到文件
rotating_logger = logging.getLogger(name="rotatingFileLogger")

file_logger.debug("test11")
rotating_logger.debug("test222")
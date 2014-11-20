setwd("~/SparkleShare")
dirs  <- basename(list.dirs(recursive = FALSE))
for (i in dirs) {
        id  <- as.character(read.table(file.path(getwd(), i, ".sparkleshare")))
        cat("  <folder>", "\n", file = "config.xml", append = TRUE, sep = "")
        cat("    <name>", i ,"</name>", "\n",  file = "config.xml", append = TRUE, sep = "")
        cat("    <identifier>", id, "</identifier>","\n",  file = "config.xml", append = TRUE, sep = "")
        cat("    <url>ssh://git@github.com/bwtian/",i,"</url>", "\n",  file = "config.xml", append = TRUE, sep = "")
        cat("    <backend>Git</backend>", "\n",  file = "config.xml", append = TRUE, sep = "")
        cat("  </folder>", "\n",  file = "config.xml", append = TRUE, sep = "")
}
              
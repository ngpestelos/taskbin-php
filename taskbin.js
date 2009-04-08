{
  "language" : "javascript",
  "views"    : {
    "inbox"  : {
      "map"  : "function(doc){if (doc.type=='inbox') emit (doc.posted, doc)}"
    }
  }
}

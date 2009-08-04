require 'rubygems'
require 'couchrest'

couch = CouchRest.new('http://127.0.0.1:5984')
db = couch.database('taskbin')

all = {
  :map => 'function(doc) {
    for(var i = 0; i < doc.tags.length; i++)
      emit(doc.tags[i], doc);
  }'
}

type = {
  :map => 'function(doc) {
    for(var i = 0; i < doc.tags.length; i++)
      emit([doc.type, doc.tags[i]], doc);
  }'
}

db.delete_doc db.get('_design/tagged_tasks') rescue nil

db.save_doc({
  "_id"    => "_design/tagged_tasks",
  :views   => { :all => all, :type => type }
})

require 'rubygems'
require 'couchrest'

couch = CouchRest.new('http://127.0.0.1:5984')
db = couch.database('taskbin')

def by_type(type)
  {
    :map => "function(doc) {
      if (doc.type == \"#{type}\")
        emit(Date.parse(doc.updated), doc);
    }"
  }
end

db.delete_doc db.get('_design/tasks') rescue nil

db.save_doc({
  "_id"  => "_design/tasks",
  :views => { :inbox => by_type(:inbox), :next => by_type(:next), :someday => by_type(:someday), :trash => by_type(:trash) }
})

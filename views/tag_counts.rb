require 'rubygems'
require 'couchrest'

couch = CouchRest.new('http://127.0.0.1:5984')
db = couch.database('taskbin')

tc = {
  :map => 'function(doc) {
    for (var i = 0; i < doc.tags.length; i++)
      emit(doc.tags[i], 1);
  }',
  :reduce => 'function(tag, count) {
    return sum(count);
  }'
}

db.delete db.get('_design/tag_counts') rescue nil

db.save_doc({
  "_id"    => "_design/tag_counts",
  :views   => { :all => tc }
})

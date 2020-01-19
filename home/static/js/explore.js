var subtopics = [];
{% for x in Subtopics %}
subtopics.push({selection:"no", name:'{{ x.name }}', link:"{% url 'explore:subtopic' subtopic=x.name|custom_url %}"},)
{% endfor %}
for (var x = 0; x < subtopics.length; x++) {
if (subtopics[x].name=='{{ section.name }}') {
  subtopics[x].selection = 'yes';
}
}
var articles = []
{% for x in section.article_set.all %}
articles.push({usually:"10", question:'{{ x.article }}', background:"https://cdn-images-1.medium.com/max/1200/0*oz2e-hQtsHOWzoB4.", link:"{% url 'explore:article' subtopic=section.name|custom_url article=x.article|custom_url %}", difficulty:"Easy"},)
{% endfor %}
var app = angular.module("myApp",[]);
app.controller("myCtrl", function($scope){
$scope.myObj = subtopics
$scope.myObj2 = articles
});
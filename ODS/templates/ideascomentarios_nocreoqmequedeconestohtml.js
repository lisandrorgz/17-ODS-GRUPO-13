html
/* Comments
----------------------------------------------- */
.comments .comments-content .icon.blog-author {
background-repeat: no-repeat;
background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEgAACxIB0t1+/AAAAAd0SU1FB9sLFwMeCjjhcOMAAAD+SURBVDjLtZSvTgNBEIe/WRRnm3U8RC1neQdsm1zSBIU9VVF1FkUguQQsD9ITmD7ECZIJSE4OZo9stoVjC/zc7ky+zH9hXwVwDpTAWWLrgS3QAe8AZgaAJI5zYAmc8r0G4AHYHQKVwII8PZrZFsBFkeRCABYiMh9BRUhnSkPTNCtVXYXURi1FpBDgArj8QU1eVXUzfnjv7yP7kwu1mYrkWlU33vs1QNu2qU8pwN0UpKoqokjWwCztrMuBhEhmh8bD5UDqur75asbcX0BGUB9/HAMB+r32hznJgXy2v0sGLBcyAJ1EK3LFcbo1s91JeLwAbwGYu7TP/3ZGfnXYPgAVNngtqatUNgAAAABJRU5ErkJggg==);
}
.comments .comments-content .loadmore a {
background: transparent url(//www.blogblog.com/1kt/ethereal/white-fade.png) repeat-x scroll top left;
}
.comments .comments-content .loadmore a {
border-top: 1px solid #0b5394;
border-bottom: 1px solid #0b5394;
}
.comments .comment-thread.inline-thread {
background: transparent url(//www.blogblog.com/1kt/ethereal/white-fade.png) repeat-x scroll top left;
}
.comments .continue {
border-top: 2px solid #0b5394;
}




<div class='comments' id='comments'>
<a name='comments'></a>
<h4>1 comentario:</h4>
<div class='comments-content'>
<script async='async' src='' type='text/javascript'></script>
<script type='text/javascript'>
(function() {
      var items = null;
      var msgs = null;
      var config = {};

// <![CDATA[
      var cursor = null;
      if (items && items.length > 0) {
        cursor = parseInt(items[items.length - 1].timestamp) + 1;
      }

      var bodyFromEntry = function(entry) {
        var text = (entry &&
                    ((entry.content && entry.content.$t) ||
                     (entry.summary && entry.summary.$t))) ||
            '';
        if (entry && entry.gd$extendedProperty) {
          for (var k in entry.gd$extendedProperty) {
            if (entry.gd$extendedProperty[k].name == 'blogger.contentRemoved') {
              return '<span class="deleted-comment">' + text + '</span>';
            }
          }
        }
        return text;
      }

      var parse = function(data) {
        cursor = null;
        var comments = [];
        if (data && data.feed && data.feed.entry) {
          for (var i = 0, entry; entry = data.feed.entry[i]; i++) {
            var comment = {};
            // comment ID, parsed out of the original id format
            var id = /blog-(\d+).post-(\d+)/.exec(entry.id.$t);
            comment.id = id ? id[2] : null;
            comment.body = bodyFromEntry(entry);
            comment.timestamp = Date.parse(entry.published.$t) + '';
            if (entry.author && entry.author.constructor === Array) {
              var auth = entry.author[0];
              if (auth) {
                comment.author = {
                  name: (auth.name ? auth.name.$t : undefined),
                  profileUrl: (auth.uri ? auth.uri.$t : undefined),
                  avatarUrl: (auth.gd$image ? auth.gd$image.src : undefined)
                };
              }
            }
            if (entry.link) {
              if (entry.link[2]) {
                comment.link = comment.permalink = entry.link[2].href;
              }
              if (entry.link[3]) {
                var pid = /.*comments\/default\/(\d+)\?.*/.exec(entry.link[3].href);
                if (pid && pid[1]) {
                  comment.parentId = pid[1];
                }
              }
            }
            comment.deleteclass = 'item-control blog-admin';
            if (entry.gd$extendedProperty) {
              for (var k in entry.gd$extendedProperty) {
                if (entry.gd$extendedProperty[k].name == 'blogger.itemClass') {
                  comment.deleteclass += ' ' + entry.gd$extendedProperty[k].value;
                } else if (entry.gd$extendedProperty[k].name == 'blogger.displayTime') {
                  comment.displayTime = entry.gd$extendedProperty[k].value;
                }
              }
            }
            comments.push(comment);
          }
        }
        return comments;
      };

      var paginator = function(callback) {
        if (hasMore()) {
          var url = config.feed + '?alt=json&v=2&orderby=published&reverse=false&max-results=50';
          if (cursor) {
            url += '&published-min=' + new Date(cursor).toISOString();
          }
          window.bloggercomments = function(data) {
            var parsed = parse(data);
            cursor = parsed.length < 50 ? null
                : parseInt(parsed[parsed.length - 1].timestamp) + 1
            callback(parsed);
            window.bloggercomments = null;
          }
          url += '&callback=bloggercomments';
          var script = document.createElement('script');
          script.type = 'text/javascript';
          script.src = url;
          document.getElementsByTagName('head')[0].appendChild(script);
        }
      };
      var hasMore = function() {
        return !!cursor;
      };
      var getMeta = function(key, comment) {
        if ('iswriter' == key) {
          var matches = !!comment.author
              && comment.author.name == config.authorName
              && comment.author.profileUrl == config.authorUrl;
          return matches ? 'true' : '';
        } else if ('deletelink' == key) {
          return config.baseUri + '/delete-comment.g?blogID='
               + config.blogId + '&postID=' + comment.id;
        } else if ('deleteclass' == key) {
          return comment.deleteclass;
        }
        return '';
      };

      var replybox = null;
      var replyUrlParts = null;
      var replyParent = undefined;

      var onReply = function(commentId, domId) {
        if (replybox == null) {
          // lazily cache replybox, and adjust to suit this style:
          replybox = document.getElementById('comment-editor');
          if (replybox != null) {
            replybox.height = '250px';
            replybox.style.display = 'block';
            replyUrlParts = replybox.src.split('#');
          }
        }
        if (replybox && (commentId !== replyParent)) {
          replybox.src = '';
          document.getElementById(domId).insertBefore(replybox, null);
          replybox.src = replyUrlParts[0]
              + (commentId ? '&parentID=' + commentId : '')
              + '#' + replyUrlParts[1];
          replyParent = commentId;
        }
      };

      var hash = (window.location.hash || '#').substring(1);
      var startThread, targetComment;
      if (/^comment-form_/.test(hash)) {
        startThread = hash.substring('comment-form_'.length);
      } else if (/^c[0-9]+$/.test(hash)) {
        targetComment = hash.substring(1);
      }

      // Configure commenting API:
      var configJso = {
        'maxDepth': config.maxThreadDepth
      };
      var provider = {
        'id': config.postId,
        'data': items,
        'loadNext': paginator,
        'hasMore': hasMore,
        'getMeta': getMeta,
        'onReply': onReply,
        'rendered': true,
        'initComment': targetComment,
        'initReplyThread': startThread,
        'config': configJso,
        'messages': msgs
      };

      var render = function() {
        if (window.goog && window.goog.comments) {
          var holder = document.getElementById('comment-holder');
          window.goog.comments.render(holder, provider);
        }
      };

      // render now, or queue to render when library loads:
      if (window.goog && window.goog.comments) {
        render();
      } else {
        window.goog = window.goog || {};
        window.goog.comments = window.goog.comments || {};
        window.goog.comments.loadQueue = window.goog.comments.loadQueue || [];
        window.goog.comments.loadQueue.push(render);
      }
    })();
// ]]>
  </script>
<div id='comment-holder'>
<div class="comment-thread toplevel-thread"><ol id="top-ra"><li class="comment" id="c8195449246400116162"><div class="avatar-image-container"><img src="//resources.blogblog.com/img/blank.gif" alt=""/></div><div class="comment-block"><div class="comment-header"><cite class="user">Anónimo</cite><span class="icon user "></span><span class="datetime secondary-text"><a rel="nofollow" href="http://pruebasanyelguti.blogspot.com/p/blog-page.html">30/12/14 2:07 a.&#160;m.</a></span></div><p class="comment-content">Prmer comentario de prueba como usuario anónimo</p><span class="comment-actions secondary-text"><a class="comment-reply" target="_self" data-comment-id="8195449246400116162">Responder</a><span class="item-control blog-admin blog-admin pid-850835007"><a target="_self" href="https://www.blogger.com/delete-comment.g?blogID=3798859254045366452&amp;postID=8195449246400116162">Eliminar</a></span></span></div><div class="comment-replies"><div id="c8195449246400116162-rt" class="comment-thread inline-thread hidden"><span class="thread-toggle thread-expanded"><span class="thread-arrow"></span><span class="thread-count"><a target="_self">Respuestas</a></span></span><ol id="c8195449246400116162-ra" class="thread-chrome thread-expanded"><div></div><div id="c8195449246400116162-continue" class="continue"><a class="comment-reply" target="_self" data-comment-id="8195449246400116162">Responder</a></div></ol></div></div><div class="comment-replybox-single" id="c8195449246400116162-ce"></div></li></ol><div id="top-continue" class="continue"><a class="comment-reply" target="_self">Añadir comentario</a></div><div class="comment-replybox-thread" id="top-ce"></div><div class="loadmore hidden" data-post-id="4883578343044831620"><a target="_self">Cargar más...</a></div></div>
</div>
</div>
<p class='comment-footer'>
<div class='comment-form'>
<a name='comment-form'></a>
<p>
</p>
<a href='https://www.blogger.com/comment-iframe.g?blogID=3798859254045366452&pageID=4883578343044831620' id='comment-editor-src'></a>
<iframe allowtransparency='true' class='blogger-iframe-colorize blogger-comment-from-post' frameborder='0' height='410px' id='comment-editor' name='comment-editor' src='' width='100%'></iframe>
<script src='https://www.blogger.com/static/v1/jsbin/3261120736-comment_from_post_iframe.js' type='text/javascript'></script>
<script type='text/javascript'>BLOG_CMT_createIframe('https://www.blogger.com/rpc_relay.html'); </script>


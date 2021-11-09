### App.vue

```vue
<template>
  <div id="app" class="container">
    <search-bar @search="onSearch"></search-bar>

    <div class="row">
      <video-detail
        class="col-8"
        :selectedVideo="selectedVideo"
      >
      </video-detail>

      <video-list
        :videos="videos"
        class="col-4"
        @select-video="selectVideo"
      >
      </video-list>
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'App',
  data: function () {
    return {
      videos: [],
      searchingWord: '',
      selectedVideo: null,
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail
  },
  methods: {
    onSearch (userInput) {
      this.searchingWord = userInput
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      // env 로드는 서버를 껐다켜야 가능!
      const API_KEY = process.env.VUE_APP_API_KEY

      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.searchingWord,
      }
      console.log(params)
      axios({
        method: 'get',
        url: API_URL,
        params
      })
        .then(response => {
          console.log(response)
          this.videos = response.data.items
          this.videos.forEach(video => {
            video.snippet.title = _.unescape(video.snippet.title)
          })
        })
    },
    selectVideo(video){
      this.selectedVideo = video
    }
  }
}
</script>
```



### SearchBar.vue

```vue
<template>
  <div>
    <input type="text" @keyup.enter="onSearch">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onSearch (event) {
      this.$emit('search', event.target.value)
    }
  }
}
</script>
```



### VideoList.vue

```vue
<template>
  <ul>
    <video-list-item
      v-for="video in videos"
      :key="video.id.videoId"
      :video="video"
      @select-video="selectVideo"
    >
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  props: {
    videos: Array,
  },
  components: {
    VideoListItem,
  },
  methods: {
    selectVideo(video){
      this.$emit('select-video', video)
    }
  }
}
</script>
```



### VideoListItem.vue

```vue
<template>
  <li @click="selectVideo" class="row">
    <img :src="video.snippet.thumbnails.default.url" :alt="videoTitle" class="col-4">
    <p class="col-8">{{ videoTitle }}</p>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    videoTitle () {
      return this.video.snippet.title
    }
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  },
}
</script>
```



### VideoDetail.vue

```vue
<template>
  <div v-if="selectedVideo">
    <iframe :src="videoURL" frameborder="0"></iframe>
    <h3>{{ selectedVideo.snippet.title }}</h3>
    <p>{{ selectedVideo.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    selectedVideo: Object,
  },
  computed: {
    videoURL () {
      const id = this.selectedVideo.id.videoId
      return `https://www.youtube.com/embed/${id}`
    }
  },
}
</script>
```


<template>
  <div class="back">
    <router-link to="/selectcountry" class="routback">⬅</router-link>
    <h3>Choose your News Sources</h3>
  </div>

  <div class="searchbar">
    <input type="text" placeholder="Search" class="w" v-model="searchText" />
    <i class="search-icon fas fa-search"></i>
  </div>

  <div class="topics">
    <div v-for="topic in filteredTopics" :key="topic.id" class="topic">
      <h2>{{ topic.name }}</h2>
    </div>
  </div>

  <div class="button-container">
    <button type="button" class="btn btn-primary btnforgot" @click="goto">
      Next
    </button>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.search-container {
  margin-bottom: 20px;
}

.search {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.back {
  display: flex;
  justify-content: space-evenly;
  align-items: flex-start;
  font-size: 20px;
  margin-top: 30px;
  margin-right: 45px;
}
.routback {
  text-decoration: none;
  color: #4e4b66;
  margin-right: 10px;
}

.search-container {
  position: relative;
}

.search-icon {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  color: #4e4b66;
}
.searchbar {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 10px;
}
.w {
  width: 85%;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #4e4b66;
  outline: none;
  font-size: 16px;
  color: #4e4b66;
}
.button-container {
  display: flex;
  justify-content: center;
}
@media (max-width: 992px) {
  .button-container {
    margin-top: 17rem;
  }
}

/* For mobile phones */
@media (max-width: 380px) {
  .button-container {
    margin-top: 0rem;
  }
}
@media (max-width: 320px) {
  .button-container {
    margin-top: 0rem;
  }
}
.btnforgot {
  width: 90%;
  height: 45px;
  font-weight: 700;
}
</style>

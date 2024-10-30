export const api = {
  async getMe() {
    return fetch('http://localhost:8000/users/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json(); // 解析 JSON 数据
      })
      .then(data => {
        console.log('User data:', data); // 处理获取到的数据
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
  },
};

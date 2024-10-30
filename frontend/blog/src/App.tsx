import { api } from './api/api'
import './App.scss';

function App() {

  return (
    <div>
      <div className='btn' onClick={() => {
        api.getMe()
      }}>
        请求一下users
      </div>
    </div>
  )
}

export default App;

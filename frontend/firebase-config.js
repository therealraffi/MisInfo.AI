// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA6HFr_Iml1ROu_jtzNMQQmP13Rxm-eWms",
  authDomain: "hoohacks2024-ffe59.firebaseapp.com",
  projectId: "hoohacks2024-ffe59",
  storageBucket: "hoohacks2024-ffe59.appspot.com",
  messagingSenderId: "908790137444",
  appId: "1:908790137444:web:eee1347e77fc33dc31d571",
  measurementId: "G-C5JM31T6PH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
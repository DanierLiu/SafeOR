import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Link from 'next/link';
import { getSortedPostsData } from '../lib/posts';
import Layout from '../components/layout';
import { useState } from "react"; 

export async function getStaticProps() {
  const allPostsData = getSortedPostsData();
  return {
    props: {
      allPostsData,
    },
  };
}

export default function Home({ allPostsData }) {
const [showPopup, setShowPopup] = useState(false);

  async function handleClick() {
    setShowPopup(true);

    const data = await fetch('url')
  }

  return (
   
    <div className={styles.container} id="main_content">
   
      <Head>
        <title>SafeOR</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <img class="mt-10" src= "images/logo.jpg" />
      <p class="text-[#5CC3C6] text-6xl mt-10 mb-5">Shaping technology to save lives</p>
     <div style={{display: showPopup ? "none" : "block"}}>
        <button onClick={handleClick} id="script" class="bg-[#5CC3C6] text-white font-bold  rounded-full m-5 " >
          Start Procedure
        </button>
      </div>
      <div style={{position: 'absolute', "background-color": "white", width:"100%", height:"100%", display: showPopup ? "block" : "none" }}
      className="fixed w-screen h-screen ">
        <p>Processing</p>
      </div>

              <Link href="/report">
        <button class="bg-[#5CC3C6] text-white font-bold  rounded-full ">
          View Report
        </button>
      </Link>

      <h3 class="align-center font-bold text-3xl mt-20">What is SafeOR? </h3>
      <h4 class="text-m mr-10 ml-10 mt-10">SafeOR uses modern technologies such as computer vision, NLP, and machine learning to bring visibility to the patient safety and need for tech enabled solutions to reduce medical error.
      When we look the numbers of deaths that are caused due to medical error, they are at an insane amount and do not seem to be decreasing. <b> How we do it? </b> We worked the computer to <b>recognize patterns of fatigue, and incompetence 
      if any caused by external factors. </b>The computer, combined with a high definition lens fitted in the operating room is able to track those patterns and tackle some of those challenges real-time with feedback and some through
      a report generate at the end of every procedure.  </h4>
      <Link href="/faq">
        <button class="bg-[#5CC3C6] text-white font-bold  rounded-full m-5">
         FAQ
        </button>
        </Link>
        <div class='footer'>Developed by Danielx2, Kelly and Abhitej.</div>
    </div>
    
  )
}

-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: boolean_search
-- ------------------------------------------------------
-- Server version	5.7.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) DEFAULT NULL,
  `link` varchar(500) NOT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES (1,'What Is The Dark Web?','http://www.iflscience.com/technology/what-dark-web/','The “dark web” is a part of the world wide web that requires special software to access. Once inside, web sites and other services can be accessed through a browser in much the same way as the normal web. However, some sites are effectively “hidden”, in that they have not been indexed by a search engine and can only be accessed if you know the address of the site. Special markets also operate within the dark web called, “darknet markets”, which mainly sell illegal products like drugs and firearms, paid for in the cryptocurrency Bitcoin. There is even a crowdfunded “Assassination Market”, where users can pay towards having someone assassinated. Because of the the dark web’s almost total anonymity, it has been the place of choice for groups wanting to stay hidden online from governments and law enforcement agencies. On the one hand there have been whistleblowers using the dark web to communicate with journalists, but more frequently it has been used by paedophile groups, terrorists and criminals to keep their dealings secret.  Going Dark There are a number of ways to access the dark web, including the use of Tor, Freenet and I2P. Of these, the most popular is Tor (originally called The Onion Router), partly because it is one of the easiest software packages to use. Tor downloads as a bundle of software that includes a version of Firefox configured specifically to use Tor. Tor provides secrecy and anonymity by passing messages through a network of connected Tor relays, which are specially configured computers. As the message hops from one node to another, it is encrypted in a way that each relay only knows about the machine that sent the message and the machine it is being sent to. Rather than conventional web addresses, Tor uses “onion” addresses, which further obsure the content. There are even special versions of search engines like Bing and Duck Duck Go that will return onion addresses for Tor services. It is a mistake to think that Tor is entirely anonymous. If a web site is accessed, it can still potentially find out information about whoever is accessing the site because of information that is shared, such as usernames and email addresses. Those wanting to stay completely anonymous have to use special anonymity services to hide their identity in these cases.  The real deal is only virtual. Antana/Flickr, CC BY-SA Services on the dark web would not have been as popular without a means of paying for them. This is something that Bitcoin has made possible. A recent study by Carnegie Mellon researchers Kyle Soska and Nicolas Christin has calculated that drug sales on the dark net total US$100 million a year. Most, if not all, was paid for in Bitcoin. Bitcoin is made even more difficult to track on the dark web through the use of “mixing services” like Bitcoin Laundry, which enables Bitcoin transactions to be effectively hidden completely.  How ‘Dark’ Is The Dark Web? The developers of Tor and organisations like the Electronic Frontier Foundation (EFF argue that the principal users of Tor are activists and people simply concerned with maintaining their privacy. Certainly, Tor has been used in the past for journalists to talk to whistleblowers and activists, including Edward Snowden). However, even a cursory glance at the Hidden Wiki – the main index of dark websites – reveals that the majority of sites listed are concerned with illegal activities. Some of these sites are scams, and so it is not clear how easy it is to buy guns, fake passports and hire hackers from the services listed. But there are likely sites on the dark web where these things are entirely possible. Although the dark web makes law enforcement agencies’ jobs much more difficult, they have had a great deal of success in bringing down sites and arresting their users and the people behind them. The most famous of these was the arrest of Ross Ulbricht, the person behind the most well known of the drug markets, Silk Road. More recently, the FBI’s arrest of two users of a child abuse site on the dark web highlighted that they are now able to use a range of techniques to unmask Tor users’ real internet addresses.  David Glance is Director of UWA Centre for Software Practice at University of Western Australia This article was originally published on The Conversation. Read the original article. Sign up today to get weekly science coverage direct to your inbox This website uses cookies This website uses cookies to improve user experience. By continuing to use our website you consent to all cookies in accordance with our cookie policy. '),(2,'Curious about the \'deep web\'? Here\'s what you should know','https://wtop.com/cyber-security/2017/11/curious-deep-web-heres-know/','Despite many representations of a nefarious underground operating out-of-sight, the deep web is mostly benign private databases and web resources not meant to be accessed by the general public. The “surface web” is essentially what can be indexed by search engines such as Google or Bing, while the “deep web” consists of items that can’t be accessed using a search engine through a standard web browser. Protected internet databases like those for banks, anything past a login screen like your private files stored in the cloud, and data stored by private companies aren’t indexed by search engines. Websites can also specifically tell the search engines that they don’t want to be indexed, making them relatively “invisible” to the average user. Most estimates put the deep web in the 90 percent range of the entire internet, because so much of what is stored online is protected information that requires some form of authentication or knowledge of a hidden web address. There is a very small percentage of the deep web where secret, and sometimes nefarious, activity is taking place, often referred to as the “dark web” or the “darknet.”\n The tools used to access the dark web focus on anonymity by incorporating encryption and specialized privacy browsers like Tor. Also known as “The Onion Router,” Tor uses a large network of relays to bounce internet traffic through; it’s much like the layers of an onion, to make it much more difficult for anyone conducting any type of surveillance to see who is doing what. The core technology used in Tor was actually developed by the U.S. Naval Research Lab in the mid ’90s for use by the intelligence community for protecting online communications. To this day, Tor and other similar tools are used by governments, activists and whistleblowers to communicate anonymously. The Tor Project states: “Tor users include ‘normal people’ who wish to keep their internet activities private from websites and advertisers, people concerned about cyber-spying, users who are evading censorship such as activists, journalists and military professionals.” Using Tor alone doesn’t mean you’re completely anonymous, and for most users, the trade off in slow performance isn’t worth the increase in privacy for daily surfing. Tor and other similar tools are also being used for illicit activities such as buying and selling drugs, stolen credit card numbers, stolen IDs, money laundering and more via black markets only accessible on the dark web. One of the most famous dark web marketplaces was called Silk Road, which was shut down by the FBI in 2013. The site’s founder, Ross Ulbricht, was sentenced to life in prison without possibility of parole. Despite law enforcement attempts to control illegal underground marketplaces, when one is shut down, two more seem to pop up. To be fair, not all dark web resources operate in an illegal manner, and much of the activity taking place is vital to the efforts of law enforcement and the intelligence community. As with any technology, it’s impossible to control its uses for only legal purposes; so, as always, it’s the good with the bad. Ken Colburn is founder and CEO of Data Doctors Computer Services. Ask any tech question on Facebook or Twitter. Like WTOP on Facebook and follow @WTOP on Twitter to engage in conversation about this article and others. © 2017 WTOP. All Rights Reserved. Need a break? Play a quick game of solitaire or Sudoku. Or take one of our fun quizzes! '),(3,'What is cloud computing? - Definition from WhatIs.com','http://searchcloudcomputing.techtarget.com/definition/cloud-computing','Cloud computing is a general term for the delivery of hosted services over the internet. Cloud computing enables companies to consume a compute resource, such as a virtual machine (VM), storage or an application, as a utility -- just like electricity -- rather than having to build and maintain computing infrastructures in house. It has become a daunting task for IT administrators to determine which, if any, cloud provider is right for their enterprise. This exclusive guide walks readers through the benefits of using public cloud services, how to weigh the pros and cons of each cloud provider, and more. You forgot to provide an Email Address. This email address doesn’t appear to be valid. This email address is already registered. Please login. You have exceeded the maximum character limit. Please provide a Corporate E-mail Address. By submitting my Email address I confirm that I have read and accepted the Terms of Use and Declaration of Consent.  By submitting your personal information, you agree that TechTarget and its partners may contact you regarding relevant content, products and special offers.  You also agree that your personal information may be transferred and processed in the United States, and that you have read and agree to the Terms of Use and the Privacy Policy. Cloud computing boasts several attractive benefits for businesses and end users. Five of the main benefits of cloud computing are: Cloud computing services can be private, public or hybrid. Private cloud services are delivered from a business\'s data center to internal users. This model offers the versatility and convenience of the cloud, while preserving the management, control and security common to local data centers. Internal users may or may not be billed for services through IT chargeback. Common private cloud technologies and vendors include VMware and OpenStack. In the public cloud model, a third-party cloud service provider delivers the cloud service over the internet. Public cloud services are sold on demand, typically by the minute or hour, though long-term commitments are available for many services. Customers only pay for the CPU cycles, storage or bandwidth they consume. Leading public cloud service providers include Amazon Web Services (AWS), Microsoft Azure, IBM and Google Cloud Platform. A hybrid cloud is a combination of public cloud services and an on-premises private cloud, with orchestration and automation between the two. Companies can run mission-critical workloads or sensitive applications on the private cloud and use the public cloud to handle workload bursts or spikes in demand. The goal of a hybrid cloud is to create a unified, automated, scalable environment that takes advantage of all that a public cloud infrastructure can provide, while still maintaining control over mission-critical data. In addition, organizations are increasingly embracing a multicloud model, or the use of multiple infrastructure-as-a-service providers. This enables applications to migrate between different cloud providers or to even operate concurrently across two or more cloud providers. Organizations adopt multicloud for various reasons. For example, they could do so to minimize the risk of a cloud service outage or to take advantage of more competitive pricing from a particular provider. Multicloud implementation and application development can be a challenge because of the differences between cloud providers\' services and application program interfaces (APIs). Multicloud deployments should become easier, however, as providers\' services and APIs converge and become more homogeneous through industry initiatives such as the Open Cloud Computing Interface. Although cloud computing has changed over time, it has been divided into three broad service categories: infrastructure as a service (IaaS), platform as a service (PaaS) and software as a service (SaaS). IaaS providers, such as AWS, supply a virtual server instance and storage, as well as APIs that enable users to migrate workloads to a VM. Users have an allocated storage capacity and can start, stop, access and configure the VM and storage as desired. IaaS providers offer small, medium, large, extra-large and memory- or compute-optimized instances, in addition to customized instances, for various workload needs. In the PaaS model, cloud providers host development tools on their infrastructures. Users access these tools over the internet using APIs, web portals or gateway software. PaaS is used for general software development, and many PaaS providers host the software after it\'s developed. Common PaaS providers include Salesforce\'s Force.com, AWS Elastic Beanstalk and Google App Engine. SaaS is a distribution model that delivers software applications over the internet; these applications are often called web services. Users can access SaaS applications and services from any location using a computer or mobile device that has internet access. One common example of a SaaS application is Microsoft Office 365 for productivity and email services. Cloud providers are competitive, and they constantly expand their services to differentiate themselves. This has led public IaaS providers to offer far more than common compute and storage instances. For example, serverless, or event-driven computing is a cloud service that executes specific functions, such as image processing and database updates. Traditional cloud deployments require users to establish a compute instance and load code into that instance. Then, the user decides how long to run -- and pay for -- that instance. With serverless computing, developers simply create code, and the cloud provider loads and executes that code in response to real-world events, so users don\'t have to worry about the server or instance aspect of the cloud deployment. Users only pay for the number of transactions that the function executes. AWS Lambda, Google Cloud Functions and Azure Functions are examples of serverless computing services. Public cloud computing also lends itself well to big data processing, which demands enormous compute resources for relatively short durations. Cloud providers have responded with big data services, including Google BigQuery for large-scale data warehousing and Microsoft Azure Data Lake Analytics for processing huge data sets. Another crop of emerging cloud technologies and services relates to artificial intelligence (AI) and machine learning. These technologies build machine understanding, enable systems to mimic human understanding and respond to changes in data to benefit the business. Amazon Machine Learning, Amazon Lex, Amazon Polly, Google Cloud Machine Learning Engine and Google Cloud Speech API are examples of these services. Security remains a primary concern for businesses contemplating cloud adoption -- especially public cloud adoption. Public cloud service providers share their underlying hardware infrastructure between numerous customers, as public cloud is a multi-tenant environment. This environment demands copious isolation between logical compute resources. At the same time, access to public cloud storage and compute resources is guarded by account login credentials. Many organizations bound by complex regulatory obligations and governance standards are still hesitant to place data or workloads in the public cloud for fear of outages, loss or theft. However, this resistance is fading, as logical isolation has proven reliable, and the addition of data encryption and various identity and access management tools has improved security within the public cloud. Cloud computing traces its origins back to the 1960s, when the computer industry recognized the potential benefits of delivering computing as a service or a utility. However, early computing lacked the connectivity and bandwidth needed to implement computing as a utility. It wasn\'t until the broad availability of internet bandwidth in the late 1990s that computing as a service became practical. In the late 1990s, Salesforce offered one of the first commercially successful implementations of enterprise SaaS. This was followed closely by the arrival of AWS in 2002, offering a range of services, including storage and computation -- and now embracing databases, machine learning and other services. Today, Microsoft Azure, Google Cloud Platform and other providers have joined AWS in providing cloud-based services to individuals, small businesses and global enterprises. The true meaning of cloud computing demystified Find the most cost-effective environment for your applications Which application integration strategy is right for you? Brian Posey explains the business benefits of public cloud services, its cost considerations and provides advice for choosing the best public cloud provider Find more PRO+ content and other member only offers, here. IT industry trends: Six major vendors chart new courses Be ready for extra work when you manage multiple clouds Margaret Rouse asks: By submitting you agree to receive email from TechTarget and its partners. If you reside outside of the United States, you consent to having your personal data transferred to and processed in the United States. Privacy Common Hyper-V administration tasks are time-consuming and risk slowing down your workflow. Use these tools to simplify and ... To configure Azure AD authentication, use express settings if the application registration is already done or manual steps if you... Learn the basics of VM management with Puppet by following these examples. Puppet is a powerful tool, and with practice, it can ... VMware Integrated OpenStack features VMware support, seamless integration with the vRealize Suite and more, making it a ... When your ESXi host abruptly reboots, you can use logs to track the potential causes, whether they be planned, environmental or ... A forgotten ESXi root password can stop you in your tracks. Avoid dodgy quick fixes and learn the proper way to recover a root ... VDI shops must understand the ins and outs of remote display protocols to make sure users are having a good experience with the ... To truly evaluate whether DaaS can help their organizations, IT pros must account for the total cost of ownership and understand ... A VDI deployment is tricky enough without worrying about having the right VDI licensing. Stay one step ahead of the problems by ... AWS gave its automation capabilities a boost with the release of CloudFormation StackSets, a feature that lets dev teams deploy ... VMware Cloud on AWS provides a bare-metal option, and EC2 Dedicated Hosts offer increased isolation. But the majority of AWS ... Amazon SQS enables users to process and track tasks in a queue. Combine it with Lambda and CloudWatch to add extra message ... RHEL 7.3 offers high security, reliability and performance. Discover how to navigate GRUB 2 and system, and learn which distros ... With its own digital transformation underway, CA Technologies wants to lead legacy mainframe software users into the world of ... HCI vendors offer software-only options that allow IT to steer clear of lock-in and scalability concerns. However, commodity ... Microsoft\'s Project Honolulu puts the GUI back in the spotlight for systems administrators who felt left behind by the company\'s ... Microsoft will release a developer-focused Windows Server version twice a year. Businesses can choose between a traditional ... Don\'t let network traffic bottlenecks slow data transfer to branch office employees. There are two ways to use Windows ... It could take a lot of programming and maintenance to tailor a CRM system to a B2B or B2C company\'s market, customer base and ... Adding artificial intelligence to lead scoring can help companies increase sales by better prioritizing customers and aligning ... The marketing technology field has exploded, as have ways to organize a martech stack. This episode of the Pipeline podcast ... All Rights Reserved, \nCopyright 2010 - 2017, TechTarget\n '),(4,'What is Internet? - Definition from WhatIs.com','http://searchwindevelopment.techtarget.com/definition/Internet','The Internet, sometimes called simply \"the Net,\" is a worldwide system of computer networks - a network of networks in which users at any one computer can, if they have permission, get information from any other computer (and sometimes talk directly to users at other computers). It was conceived by the Advanced Research Projects Agency (ARPA) of the U.S. government in 1969 and was first known as the ARPANet. The original aim was to create a network that would allow users of a research computer at one university to \"talk to\" research computers at other universities. A side benefit of ARPANet\'s design was that, because messages could be routed or rerouted in more than one direction, the network could continue to function even if parts of it were destroyed in the event of a military attack or other disaster. The IoT world may be exciting, but there are serious technical challenges that need to be addressed, especially by developers. In this handbook, learn how to meet the security, analytics, and testing requirements for IoT applications. Today, the Internet is a public, cooperative and self-sustaining facility accessible to hundreds of millions of people worldwide. Physically, the Internet uses a portion of the total resources of the currently existing public telecommunication networks. Technically, what distinguishes the Internet is its use of a set of protocols called TCP/IP (for Transmission Control Protocol/Internet Protocol). Two recent adaptations of Internet technology, the intranet and the extranet, also make use of the TCP/IP protocol. For most Internet users, electronic mail (email) practically replaced the postal service for short written transactions. People communicate over the Internet in a number of other ways including  Internet Relay Chat (IRC), Internet telephony, instant messaging, video chat or social media.  The most widely used part of the Internet is the World Wide Web (often abbreviated \"WWW\" or called \"the Web\"). Its outstanding feature is hypertext, a method of instant cross-referencing. In most Web sites, certain words or phrases appear in text of a different color than the rest; often this text is also underlined. When you select one of these words or phrases, you will be transferred to the site or page that is relevant to this word or phrase. Sometimes there are buttons, images, or portions of images that are \"clickable.\" If you move the pointer over a spot on a Web site and the pointer changes into a hand, this indicates that you can click and be transferred to another site. Using the Web, you have access to billions of pages of information. Web browsing is done with a Web browser, the most popular of which are Chrome, Firefox and Internet Explorer. The appearance of a particular Web site may vary slightly depending on the browser you use. Also, later versions of a particular browser are able to render more \"bells and whistles\" such as animation, virtual reality, sound, and music files, than earlier versions. The Internet has continued to grow and evolve over the years of its existence. IPv6, for example, was designed to anticipate enormous future expansion in the number of available IP addresses. In a related development, the Internet of Things (IoT) is the burgeoning environment in which almost any entity or object can be provided with a unique identifier and the ability to transfer data automatically over the Internet. A brief explanation of how the Internet works: By submitting you agree to receive email from TechTarget and its partners. If you reside outside of the United States, you consent to having your personal data transferred to and processed in the United States. Privacy While the general benefits of public cloud, such as increased scalability, apply to mobile apps, there are other ways IaaS ... Backups are critical in any cloud strategy, but where you store that data is just as important. Explore these automated backup ... Serverless computing can boost flexibility and reduce overall cloud costs. To tap into these benefits, though, be sure to ... The DevOps journey is well underway, but many obstacles remain. New products using artificial intelligence and machine learning ... Testing the internet of things is one thing, but AI takes it to the next level. A LogiGear executive shares what the company ... A complicated new game required a complicated testing strategy and help from the outside. Here\'s what game maker Anki learned ... Oracle did a great job getting Java SE 9 released earlier this year, but modularity and various smaller updates may not be enough... At JavaOne 2017, Oracle identified four projects that will have a significant impact on the future of Java: Project Valhalla, ... Whether it is a secure cloud, a secure mobile device or a secure IOT interaction, organizations are making blockchain security a ... IBM joined the Docker MTA program to make it easier for enterprises to modernize their existing applications by using containers ... This product update explores a new database load-balancing software release, ScaleArc for SQL Server, which is integrated with ... Learn how multi-cloud architecture can help with digital transformation, despite how many single-cloud structures exist. Expert ... All Rights Reserved, \nCopyright 2000 - 2017, TechTarget\n '),(5,'Solutions for Smart Farming - Agriculture IoT Solutions and Internet of Things Technologies','https://www.kaaproject.org/agriculture/','For farmers and growers, the Internet of Things has opened up extremely productive ways to cultivate soil and raise livestock with the use of cheap, easy-to-install sensors and an abundance of insightful data they offer. Prospering on this prolific build-up of the Internet of Things in agriculture, smart farming applications are gaining ground with the promise to deliver 24/7 visibility into soil and crop health, machinery in use, storage conditions, animal behavior, and energy consumption level. The Kaa open-source IoT Platform is a crucial middleware technology that allows walking safely into the agriculture IoT field. By tying together different sensors, connected devices, and farming facilities, Kaa streamlines the development of smart farming systems to the maximum degree possible. Kaa is perfectly applicable for single-purpose smart farming products - such as smart metering devices, livestock trackers, or failure prediction systems - as well as for multi-device solutions, among which are resource mapping and farming produce analytics solutions. Kaa is feature-rich and, as an open-source platform, grants full access to its modules for any necessary modifications, extensions, or integrations. Out of the box, Kaa already provides a set of ready-to-use components for a quick start with smart farming applications. After all, farming is all about connecting with nature - leave everything else to Kaa. Sensor-based field and resource mapping Remote equipment monitoring Remote crop monitoring Predictive analytics for crops and livestock Climate monitoring and forecasting Livestock tracking and geofencing Stats on livestock feeding and produce Smart logistics and warehousing Find out more about Kaa applications for smart farming solutions Agriculture Automotive ConsumerElectronics Healthcare IndustrialIoT Logistics SmartCity SmartEnergy SmartRetail Sport & Fitness Wearables Telecom \nGitex, Dubai, 2017 \n\n\n\n\n ');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-05 16:31:11

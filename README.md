\# 6GEI311 — Laboratoire 5 : Déploiement \& Distribution de charge (Flask + Nginx)



\*\*Équipe :\*\*  

\- Membre A : Siba Guilavogui (SG) — IP: <IP\_SIBA>, port: 3000  

\- Membre B : Adama Alseny Baldé (AB) — IP: <TA\_IP>, port: 3001



\## 🔹 Ce que j’ai appris

\- Déployer une application Flask accessible sur un réseau local via IP et port.  

\- Modifier le code du coéquipier pour créer une deuxième instance du serveur.  

\- Configurer Nginx (côté membre A) pour équilibrer la charge entre les deux instances.  

\- Comprendre le mécanisme de \*\*load balancing\*\* et la \*\*tolérance aux pannes\*\*.



\## 🔹 Réponses aux questions de la manip



\### Q1 : Que voit-on quand on lance Flask ?

→ Le message “Hello, World! from SG at IP\_SIBA” sur `http://IP\_SIBA:3000/`



\### Q2 : Que se passe-t-il quand on arrête Flask ?

→ `http://IP\_SIBA:3000/` devient inaccessible (erreur de connexion).



\### Q3 : Que se passe-t-il via Nginx ?

→ Les requêtes alternent entre :

\- “Hello, World! from SG…”  

\- “Hello, World! from AB…”  

→ C’est la \*\*distribution de charge\*\*.



\### Q4 : Quand Flask A est arrêté ?

→  

\- `http://IP\_SIBA:3000/` ❌ ne répond plus  

\- `http://IP\_SIBA:8181/` ✅ fonctionne toujours  

→ Nginx redirige les requêtes vers l’application du membre B.



\## 🔹 Captures d’écran à inclure

1\. Application Flask A en marche  

2\. Application Flask B en marche  

3\. Nginx avec alternance des réponses  

4\. Nginx toujours accessible après arrêt de A






\# 6GEI311 — Laboratoire 5 : Déploiement et Distribution de charge (Flask + Nginx)



\*\*Équipe :Siba Guilavogui: GUIS15049901 ;
              Adama A Balde: BALA27070105 ;
              Ibrahima Diallo:DIAI01100203;

\*  

\- Membre A : Siba Guilavogui (SG) — IP:<172.20.10.02>,Port:3000

\- Membre B : Adama A Balde (AAB) et Ibrahima DIallo (IB) — IP: <172.20.10.13:3000>, port: 3001



\##  Objectif du laboratoire

L’objectif de ce laboratoire était de comprendre comment déployer une application web simple à l’aide de \*\*Flask\*\* et d’expérimenter la \*\*distribution de charge\*\* (load balancing) à l’aide de \*\*Nginx\*\*.  

Nous avons aussi appris à configurer deux serveurs Flask distincts sur des ports différents et à les relier à un même distributeur de charge pour assurer la répartition automatique des requêtes et la tolérance aux pannes.



---



\##  Ce que nous avons appris

Au cours de ce laboratoire, nous avons plusieurs notions importantes:



\- Comment installer et exécuter une application \*\*Flask\*\* sur une adresse IP locale et un port spécifique.  

\- Comment faire communiquer deux applications Flask sur des ports différents (par exemple 3000 et 3001).  

\- Comment configurer \*\*Nginx\*\* pour agir comme un \*\*proxy inverse (reverse proxy)\*\* et distribuer les requêtes entre deux serveurs Flask.  

\- Comment \*\*GitHub\*\* peut être utilisé pour collaborer entre deux membres d’une équipe et partager le code facilement.  

\- Le principe de \*\*tolérance aux pannes\*\* : même si un serveur s’arrête, Nginx continue de rediriger les requêtes vers le serveur encore disponible.  

\- Le rôle des fichiers de configuration (`nginx.conf`) et des ports dans la gestion du trafic web.  

\- L’importance de séparer les rôles (membre A / membre B) pour simuler un vrai environnement de déploiement collaboratif.



Ce laboratoire nous a permis de mieux comprendre comment les applications web sont déployées dans la réalité et comment les entreprises utilisent des outils comme Nginx pour rendre leurs systèmes plus robustes et plus rapides.



---



\##  Réponses aux questions de la manip



\### Q1 : Que voit-on quand on lance Flask ?

→ Le message “Hello, World! venant de SG a l'adresse IP de SIBA” sur `http://172.20.10.02:3000/`

Cela confirme que le serveur Flask fonctionne correctement sur la machine du membre A.



\### Q2 : Que se passe-t-il quand on arrête Flask ?

→ `http://172.20.10.02:3000/` devient inaccessible (erreur de connexion).

Cela signifie que le service Flask ne répond plus, car le serveur web n’est plus en écoute sur ce port.



\### Q3 : Que se passe-t-il via Nginx ?

→ Les requêtes alternent entre :

\- “Hello, World! venant de SG a l'adresse172.20.10.02”  

\- “Hello, World! from AAB a l'adresse 172.20.10.13:3000”  

Cela montre que Nginx distribue automatiquement les requêtes entre les deux serveurs Flask



\### Q4 : Quand Flask A est arrêté ?

→  

\- `http://172.20.10.02:3000/`  ne répond plus 

\- `http://172.20.10.13:3001/`  fonctionne toujours

\- `http://172.20.10.02:8181/`  fonctionne toujours  

Cela prouve que Nginx redirige automatiquement les requêtes vers le serveur disponible, assurant ainsi la tolérance aux pannes.



---



\## Conclusion



En résumé, ce laboratoire m’a permis de comprendre les bases du déploiement d’applications web et du load balancing.

J’ai appris à :



Démarrer et configurer une application Flask.



Configurer un serveur Nginx pour répartir le trafic.



Tester la répartition et la redondance des serveurs.



Collaborer efficacement via GitHub sur un même projet.



Ce laboratoire m’a donné une vision concrète du fonctionnement des serveurs web dans un environnement professionnel où la fiabilité et la disponibilité sont essentielles.






import './graphiqueContrats.style.css'

const GraphiqueContrats = ({data}) => {
    let transformedData = [];

    if (data && data.length > 0) {
      transformedData = data.reduce((acc, objet) => {
        let dateMEPContrat = objet.DateMEPContrat;
  
        if (dateMEPContrat) {
          let [jour, mois, annee] = dateMEPContrat.split("/");
          let year = new Date(annee, mois - 1, jour).getFullYear();
  
          if (!acc[year]) {
            acc[year] = {
              DateMEPContrat: year,
              typeContrat: {},
              TotalContrat: 0,
            };
          }
  
          if (!acc[year].typeContrat[objet.CODE_CONTRAT_DIVALTO]) {
            acc[year].typeContrat[objet.CODE_CONTRAT_DIVALTO] = 0;
          }
  
          acc[year].typeContrat[objet.CODE_CONTRAT_DIVALTO]++;
          acc[year].TotalContrat++; // Incrémenter le total des contrats pour cette année
        }
  
        return acc;
      }, {});
  
      // Transformer l'objet en tableau d'objets avec la propriété TotalContrat
      transformedData = Object.entries(transformedData).map(([key, value]) => {
        return {
          ...value,
          TotalContrat: Object.values(value.typeContrat).reduce(
            (a, b) => a + b,
            0
          ),
        };
      });
    }
  
  console.log(transformedData);
  
    // Collecte de toutes les clés uniques de typeContrat
    const allKeys = transformedData.reduce((acc, item) => {
      Object.keys(item.typeContrat).forEach((key) => {
        if (!acc.includes(key)) {
          acc.push(key);
        }
      });
      return acc;
    }, []);
    allKeys.sort(); // Tri des clés par ordre alphabétique
  
    return(
        <div className="Graphiquecontrat-container">
            graphique contrat container
        </div>
    )
}

export default GraphiqueContrats
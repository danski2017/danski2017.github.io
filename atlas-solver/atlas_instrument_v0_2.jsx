import { useState, useRef, useEffect } from "react";
import * as THREE from 'three';

const SOLAR_SYSTEM = [
  { id:"SOL",     name:"Sun",     cls:"star_G2",     mass_msun:1.0,     dist_au:0 },
  { id:"MERCURY", name:"Mercury", cls:"planet",      mass_msun:1.65e-7, dist_au:0.39 },
  { id:"VENUS",   name:"Venus",   cls:"planet",      mass_msun:2.45e-6, dist_au:0.72 },
  { id:"EARTH",   name:"Earth",   cls:"planet",      mass_msun:3.00e-6, dist_au:1.00 },
  { id:"MOON",    name:"Moon",    cls:"moon",        mass_msun:3.69e-8, dist_au:1.00 },
  { id:"MARS",    name:"Mars",    cls:"planet",      mass_msun:3.23e-7, dist_au:1.52 },
  { id:"JUPITER", name:"Jupiter", cls:"planet",      mass_msun:9.55e-4, dist_au:5.20 },
  { id:"SATURN",  name:"Saturn",  cls:"planet",      mass_msun:2.86e-4, dist_au:9.58 },
  { id:"URANUS",  name:"Uranus",  cls:"planet",      mass_msun:4.37e-5, dist_au:19.2 },
  { id:"NEPTUNE", name:"Neptune", cls:"planet",      mass_msun:5.15e-5, dist_au:30.1 },
  { id:"PLUTO",   name:"Pluto",   cls:"dwarf_planet",mass_msun:6.6e-9,  dist_au:39.5 },
];

const GAIA_NEIGHBORS = [
  { id:"PROXIMA_CEN", name:"Proxima Centauri", cls:"M-dwarf", mass_msun:0.1221, dist_pc:1.295 },
  { id:"ALPHA_CEN_A", name:"Alpha Centauri A", cls:"G-star", mass_msun:1.1, dist_pc:1.338 },
  { id:"ALPHA_CEN_B", name:"Alpha Centauri B", cls:"K-star", mass_msun:0.907, dist_pc:1.338 },
  { id:"BARNARDS", name:"Barnard's Star", cls:"M-dwarf", mass_msun:0.144, dist_pc:1.828 },
  { id:"LUHMAN16A", name:"Luhman 16 A", cls:"brown_dwarf", mass_msun:0.032, dist_pc:1.998 },
  { id:"LUHMAN16B", name:"Luhman 16 B", cls:"brown_dwarf", mass_msun:0.027, dist_pc:1.998 },
  { id:"WISE0855", name:"WISE 0855-0714", cls:"brown_dwarf", mass_msun:0.008, dist_pc:2.231 },
  { id:"WOLF359", name:"Wolf 359", cls:"M-dwarf", mass_msun:0.09, dist_pc:2.394 },
  { id:"LALANDE21185", name:"Lalande 21185", cls:"M-dwarf", mass_msun:0.386, dist_pc:2.547 },
  { id:"SIRIUS_A", name:"Sirius A", cls:"A-star", mass_msun:2.063, dist_pc:2.637 },
  { id:"SIRIUS_B", name:"Sirius B", cls:"white_dwarf", mass_msun:1.018, dist_pc:2.637 },
  { id:"BL_CETI", name:"BL Ceti", cls:"M-dwarf", mass_msun:0.102, dist_pc:2.68 },
  { id:"UV_CETI", name:"UV Ceti", cls:"M-dwarf", mass_msun:0.1, dist_pc:2.68 },
  { id:"ROSS154", name:"Ross 154", cls:"M-dwarf", mass_msun:0.17, dist_pc:2.976 },
  { id:"ROSS248", name:"Ross 248", cls:"M-dwarf", mass_msun:0.136, dist_pc:3.162 },
  { id:"EPS_ERI", name:"Epsilon Eridani", cls:"K-star", mass_msun:0.832, dist_pc:3.218 },
  { id:"LACAILLE9352", name:"Lacaille 9352", cls:"M-dwarf", mass_msun:0.503, dist_pc:3.289 },
  { id:"ROSS128", name:"Ross 128", cls:"M-dwarf", mass_msun:0.168, dist_pc:3.374 },
  { id:"EZ_AQR_A", name:"EZ Aquarii A", cls:"M-dwarf", mass_msun:0.11, dist_pc:3.452 },
  { id:"61CYGNI_A", name:"61 Cygni A", cls:"K-star", mass_msun:0.708, dist_pc:3.497 },
  { id:"61CYGNI_B", name:"61 Cygni B", cls:"K-star", mass_msun:0.63, dist_pc:3.497 },
  { id:"STRUVE2398A", name:"Struve 2398 A", cls:"M-dwarf", mass_msun:0.342, dist_pc:3.517 },
  { id:"STRUVE2398B", name:"Struve 2398 B", cls:"M-dwarf", mass_msun:0.248, dist_pc:3.517 },
  { id:"GROOMBRIDGE34A", name:"Groombridge 34 A", cls:"M-dwarf", mass_msun:0.38, dist_pc:3.561 },
  { id:"GROOMBRIDGE34B", name:"Groombridge 34 B", cls:"M-dwarf", mass_msun:0.158, dist_pc:3.561 },
  { id:"DX_CANCRI", name:"DX Cancri", cls:"M-dwarf", mass_msun:0.09, dist_pc:3.582 },
  { id:"EPS_INDI_A", name:"Epsilon Indi A", cls:"K-star", mass_msun:0.762, dist_pc:3.622 },
  { id:"EPS_INDI_BA", name:"Epsilon Indi Ba", cls:"brown_dwarf", mass_msun:0.065, dist_pc:3.622 },
  { id:"EPS_INDI_BB", name:"Epsilon Indi Bb", cls:"brown_dwarf", mass_msun:0.053, dist_pc:3.622 },
  { id:"TAU_CETI", name:"Tau Ceti", cls:"G-star", mass_msun:0.783, dist_pc:3.65 },
  { id:"GJ1061", name:"GJ 1061", cls:"M-dwarf", mass_msun:0.113, dist_pc:3.674 },
  { id:"YZ_CETI", name:"YZ Ceti", cls:"M-dwarf", mass_msun:0.13, dist_pc:3.722 },
  { id:"LUYTEN_STAR", name:"Luyten's Star", cls:"M-dwarf", mass_msun:0.26, dist_pc:3.785 },
  { id:"TEEGARDEN", name:"Teegarden's Star", cls:"M-dwarf", mass_msun:0.089, dist_pc:3.831 },
  { id:"SCR1845", name:"SCR 1845-6357 A", cls:"M-dwarf", mass_msun:0.092, dist_pc:3.876 },
  { id:"KAPTEYN", name:"Kapteyn's Star", cls:"M-dwarf", mass_msun:0.274, dist_pc:3.934 },
  { id:"LACAILLE8760", name:"Lacaille 8760", cls:"M-dwarf", mass_msun:0.601, dist_pc:3.969 },
  { id:"KRUGER60A", name:"Kruger 60 A", cls:"M-dwarf", mass_msun:0.271, dist_pc:4.01 },
  { id:"KRUGER60B", name:"Kruger 60 B", cls:"M-dwarf", mass_msun:0.176, dist_pc:4.01 },
  { id:"ROSS614A", name:"Ross 614 A", cls:"M-dwarf", mass_msun:0.222, dist_pc:4.13 },
  { id:"VAN_MAANEN", name:"Van Maanen's Star", cls:"white_dwarf", mass_msun:0.67, dist_pc:4.334 },
  { id:"GLIESE1", name:"Gliese 1", cls:"M-dwarf", mass_msun:0.38, dist_pc:4.345 },
  { id:"WOLF424A", name:"Wolf 424 A", cls:"M-dwarf", mass_msun:0.14, dist_pc:4.392 },
  { id:"TZ_ARIETIS", name:"TZ Arietis", cls:"M-dwarf", mass_msun:0.15, dist_pc:4.461 },
  { id:"GJ687", name:"GJ 687", cls:"M-dwarf", mass_msun:0.413, dist_pc:4.53 },
  { id:"GJ674", name:"GJ 674", cls:"M-dwarf", mass_msun:0.35, dist_pc:4.547 },
  { id:"GJ440", name:"GJ 440", cls:"white_dwarf", mass_msun:0.55, dist_pc:4.626 },
  { id:"GJ1002", name:"GJ 1002", cls:"M-dwarf", mass_msun:0.117, dist_pc:4.844 },
  { id:"GJ412A", name:"GJ 412 A", cls:"M-dwarf", mass_msun:0.396, dist_pc:4.854 },
];

const ALL_SOURCES = [...SOLAR_SYSTEM, ...GAIA_NEIGHBORS];

const RUNG_INFO = {
  R0_scalar:          { label:"Gravity Boundaries",  desc:"Where one star's gravity ends and another begins" },
  R2_tidal:           { label:"Tidal Structure",      desc:"The stretching and squeezing geometry between stars" },
  SS_bones:           { label:"Star Web",             desc:"The geometric skeleton linking stars" },
  witness_skeleton:   { label:"Curvature Edges",      desc:"Where spacetime curvature character shifts" },
  eigenframe_handoff: { label:"Orientation Shifts",   desc:"Where the dominant pull direction rotates" },
};

const RUNGS = Object.keys(RUNG_INFO);

// Utilities
const slugify = s => s.toLowerCase().replace(/[^a-z0-9]+/g,"_").replace(/^_|_$/g,"");

const fibSphere = (i, n) => {
  const phi = Math.acos(1 - 2*(i+0.5)/n);
  const theta = Math.PI * (1 + Math.sqrt(5)) * i;
  return [Math.sin(phi)*Math.cos(theta), Math.cos(phi), Math.sin(phi)*Math.sin(theta)];
};

const starColor = cls => ({
  star_G2:"#FFE060", "G-star":"#FFD050", "K-star":"#FF9040", "M-dwarf":"#FF5030",
  "A-star":"#C0E0FF", white_dwarf:"#90B0FF", brown_dwarf:"#5A2A18",
  planet:"#4080C0", moon:"#909090", dwarf_planet:"#807060",
})[cls] || "#CCCCCC";

const starColorHex = cls => parseInt(starColor(cls).replace('#',''), 16);

const starSize = s => {
  if (s.id === 'SOL') return 2.2;
  if (s.cls === 'planet') return Math.max(0.15, Math.pow(s.mass_msun, 0.2) * 1.5);
  if (s.cls === 'moon') return 0.12;
  return Math.max(0.22, Math.min(1.4, Math.pow(s.mass_msun, 0.35) * 1.1));
};

const sourcePos = (s, i, n) => {
  const [fx, fy, fz] = fibSphere(i, n);
  const dist = s.dist_pc !== undefined ? s.dist_pc * 20 : (s.dist_au || 0) * 0.1;
  return [fx * dist, fy * dist, fz * dist];
};

const NEAREST_10 = GAIA_NEIGHBORS.slice().sort((a,b)=>a.dist_pc-b.dist_pc).slice(0,10).map(s=>s.id);

const SCENE_PRESETS = {
  SS: { purpose:"Gravitational geometry and tidal structure of the solar system",
         sources: new Set(SOLAR_SYSTEM.map(s=>s.id)) },
  LSN: { purpose:"Gravitational geometry and tidal structure of the local stellar neighborhood",
         sources: new Set(["SOL",...GAIA_NEIGHBORS.map(s=>s.id)]) },
};

const SYSTEM_PROMPT = `You are the Atlas Passport Builder AI. Guide researchers through declaring gravitational scene passports via natural conversation.

ATLAS DOCTRINE: Sources contribute. Datums interrogate. Ledger remembers. No modified GR. claim_status always: diagnostic_candidate_not_observational.

ROSTER: Solar system (SOL, MERCURY, VENUS, EARTH, MOON, MARS, JUPITER, SATURN, URANUS, NEPTUNE, PLUTO) + 49 Gaia stellar neighbors to 4.9 pc.

PASSPORT FIELDS: scene_id (snake_case_v0_1), purpose, regime (weak_field_gr_approximation), epoch (J2000), coordinate_frame (solar_system_barycentric_cartesian), units {mass:kg, distance:m}, node1 {mode:explicit_parent, description}, active_sources (array of exact roster IDs), datum_architecture, extraction_rungs (always full suite), claim_status.

- Be conversational, plain language, one question at a time.
- Always set extraction_rungs to full suite, never ask the user.
- Use exact roster IDs in active_sources.
- End messages with cumulative <passport_update>{ ... }</passport_update>
- When complete say: Your passport is ready to lock.` ;

const WELCOME = `Atlas Passport Builder online.\n\nRoster loaded: 11 solar system bodies + 49 Gaia stellar neighbors to 4.9 pc.\n\nDescribe the scene you want to study.`;

function PassportScreen({ onGenerate }) {
  const [messages, setMessages] = useState([{ role:"assistant", content:WELCOME }]);
  const [passport, setPassport] = useState({});
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [locked, setLocked] = useState(false);
  const [ready, setReady] = useState(false);
  const [mode, setMode] = useState("manual");
  const [selectedSources, setSelectedSources] = useState(new Set());
  const bottomRef = useRef(null);

  useEffect(() => { bottomRef.current?.scrollIntoView({ behavior:"smooth" }); }, [messages, loading]);

  const updateManual = (field, val) => setPassport(p => ({...p, [field]: val}));
  const toggleSource = id => {
    setSelectedSources(prev => {
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      setPassport(p => ({...p, active_sources:[...next]}));
      return next;
    });
  };
  const applyPreset = key => {
    const p = SCENE_PRESETS[key];
    if (!p) return;
    setSelectedSources(p.sources);
    setPassport(prev => ({...prev, purpose:p.purpose, active_sources:[...p.sources]}));
  };
  const allSources = [
    { group:"Solar System", items:SOLAR_SYSTEM },
    { group:"Stellar Neighbors", items:GAIA_NEIGHBORS.slice().sort((a,b)=>a.dist_pc-b.dist_pc) }
  ];

  const parseUpdate = t => { const m=t.match(/<passport_update>([\s\S]*?)<\/passport_update>/); if(m){try{return JSON.parse(m[1].trim())}catch{}}return null; };
  const stripUpdate = t => t.replace(/<passport_update>[\s\S]*?<\/passport_update>/g,"").trim();

  const sendAI = async () => {
    if (!input.trim()||loading||locked) return;
    const um = {role:"user",content:input.trim()};
    const hist = [...messages, um];
    setMessages(hist); setInput(""); setLoading(true);
    try {
      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method:"POST", headers:{"Content-Type":"application/json"},
        body:JSON.stringify({ model:"claude-sonnet-4-20250514", max_tokens:1000, system:SYSTEM_PROMPT,
          messages:hist.map(m=>({role:m.role,content:m.content})) })
      });
      const d = await res.json();
      const raw = d.content?.[0]?.text || "No response.";
      const upd = parseUpdate(raw);
      if (upd) setPassport(p=>({...p,...upd}));
      const txt = stripUpdate(raw);
      if (txt.includes("Your passport is ready to lock.")) setReady(true);
      setMessages(p=>[...p,{role:"assistant",content:txt}]);
    } catch { setMessages(p=>[...p,{role:"assistant",content:"Connection error."}]); }
    finally { setLoading(false); }
  };

  const onKey = e => { if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();sendAI();} };
  const fc = Object.keys(passport).length;
  const hl = json => {
    if (!json||json==="{}") return '<span style="color:#1e3452;font-style:italic">// awaiting declarations...</span>';
    return json.replace(/("(?:\\u[a-fA-F0-9]{4}|\\[^u]|[^\\"])*"(?:\s*:)?|\b(?:true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)/g, m => {
      if (/^"./.test(m)&&/:$/.test(m)) return `<span style="color:#4a9aba">${m}</span>`;
      if (/^"/.test(m)) return `<span style="color:#a0b4c4">${m}</span>`;
      if (/true|false/.test(m)) return `<span style="color:#a05080">${m}</span>`;
      if (/null/.test(m)) return `<span style="color:#2a4a60">${m}</span>`;
      return `<span style="color:#b07820">${m}</span>`;
    });
  };

  const fL = {display:"block",fontSize:13,color:"#c0ccd4",marginBottom:6,fontWeight:500};
  const fI = {width:"100%",background:"#0b0d14",border:"1px solid #14202e",color:"#a0b8cc",
    fontFamily:"var(--font-sans)",fontSize:14,padding:"7px 10px",borderRadius:5,outline:"none",boxSizing:"border-box"};

  return (
    <div style={{display:"flex",flexDirection:"column",height:"100%",fontFamily:"var(--font-sans)",fontSize:"13px",background:"#07090d",color:"#a0b8cc"}}>
      <style>{`
        @keyframes blink{0%,80%,100%{opacity:.2;transform:scale(.7)}40%{opacity:1;transform:scale(1)}}
        .dot{display:inline-block;width:5px;height:5px;border-radius:50%;background:#a07018;animation:blink 1.2s ease-in-out infinite;margin:0 2px}
        .dot:nth-child(2){animation-delay:.2s}.dot:nth-child(3){animation-delay:.4s}
        .tinp{width:100%;background:#0b0d14;border:1px solid #14202e;color:#a0b8cc;font-family:var(--font-sans);font-size:14px;padding:8px 12px;border-radius:5px;resize:none;outline:none;line-height:1.5;box-sizing:border-box}
        .tinp:focus{border-color:#6a4410}.tinp::placeholder{color:#2a4060}.tinp:disabled{opacity:.3;cursor:not-allowed}
        .ab{font-family:var(--font-sans);font-size:13px;letter-spacing:.07em;font-weight:500;padding:6px 14px;border-radius:5px;cursor:pointer;transition:all .15s;white-space:nowrap}
        .pri{background:#7a4e10;border:1px solid #7a4e10;color:#ddb870}.pri:hover{background:#8e5c18}
        .pri:disabled{background:#0d1520;border-color:#111e2c;color:#182840;cursor:not-allowed}
        .gho{background:transparent;border:1px solid #14202e;color:#c0ccd4}.gho:hover{border-color:#2a4060;color:#7aaccc;background:#090d14}
        .gho:disabled{opacity:.25;cursor:not-allowed;pointer-events:none}
        .lck{background:transparent;border:1px solid #14202e;color:#c0ccd4}
        .lck:hover{border-color:#2a6040;color:#3a9060;background:transparent}
        .lck:disabled{opacity:.25;cursor:not-allowed;pointer-events:none}
        ::-webkit-scrollbar{width:4px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:#14202e;border-radius:2px}
      `}</style>

      {/* Header */}
      <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",padding:"9px 16px",borderBottom:"1px solid #0c1620",background:"#080a10",flexShrink:0}}>
        <div style={{display:"flex",alignItems:"baseline",gap:"10px"}}>
          <span style={{fontSize:"19px",fontWeight:500,letterSpacing:".14em",color:"#a07018"}}>ATLAS</span>
        </div>
        <div style={{display:"flex",gap:"8px",alignItems:"center"}}>
          <span style={{fontSize:"13px",color:locked?"#3a8060":"#c0ccd4"}}>
            {locked?"Passport locked.":ready?"Ready to lock.":"Building in progress..."}
          </span>
          <button className="ab gho" onClick={()=>{setMessages([{role:"assistant",content:WELCOME}]);setPassport({});setInput("");setLocked(false);setReady(false);setSelectedSources(new Set());}}>Reset</button>
        </div>
      </div>

      {/* Body */}
      <div style={{display:"flex",flex:1,overflow:"hidden"}}>
        {/* Left panel */}
        <div style={{width:"46%",borderRight:"1px solid #0c1620",display:"flex",flexDirection:"column",overflow:"hidden"}}>
          <div style={{display:"flex",borderBottom:"1px solid #111d2b",flexShrink:0}}>
            {["ai","manual"].map(m=>(
              <button key={m} onClick={()=>setMode(m)} style={{
                flex:1,padding:"8px 0",fontSize:13,letterSpacing:".07em",fontWeight:500,
                fontFamily:"var(--font-sans)",cursor:"pointer",border:"none",
                borderBottom:mode===m?"2px solid #c8922a":"2px solid transparent",
                background:"transparent",color:mode===m?"#c8922a":"#c0ccd4",transition:"all .15s"
              }}>{m==="ai"?"AI Declaration":"Manual Form"}</button>
            ))}
          </div>

          {mode==="ai" ? (<>
            <div style={{flex:1,overflow:"auto",padding:"10px 14px"}}>
              {messages.map((m,i)=>(
                <div key={i} style={m.role==="user"
                  ?{background:"#0a0e18",borderLeft:"2px solid #c8922a",padding:"8px 12px",borderRadius:"0 5px 5px 0",margin:"5px 0",lineHeight:1.6,whiteSpace:"pre-wrap",color:"#a8bcc8"}
                  :{borderLeft:"2px solid #0e1a26",padding:"8px 12px",borderRadius:"0 5px 5px 0",margin:"5px 0",lineHeight:1.6,whiteSpace:"pre-wrap",color:"#506070"}
                }>{m.content}</div>
              ))}
              {loading&&<div style={{borderLeft:"2px solid #0e1a26",padding:"10px 14px",margin:"5px 0"}}><span className="dot"/><span className="dot"/><span className="dot"/></div>}
              <div ref={bottomRef}/>
            </div>
            <div style={{padding:"9px 14px",borderTop:"1px solid #0a1218",display:"flex",gap:"8px",flexShrink:0}}>
              <textarea className="tinp" rows={2} value={input} onChange={e=>setInput(e.target.value)} onKeyDown={onKey}
                placeholder={locked?"Passport is locked.":"Declare your scene..."} disabled={loading||locked} style={{flex:1}}/>
              <button className="ab pri" onClick={sendAI} disabled={!input.trim()||loading||locked} style={{alignSelf:"flex-end"}}>Send</button>
            </div>
          </>) : (
            <div style={{flex:1,overflow:"hidden",padding:"14px",display:"flex",flexDirection:"column"}}>
              {(()=>{
                const fG={marginBottom:14};
                return (<>
                  <div style={fG}>
                    <label style={fL}>Scene name</label>
                    <input style={fI} defaultValue="my scene" onChange={e=>updateManual("scene_id",slugify(e.target.value)+"_v0_1")}/>
                  </div>
                  <div style={fG}>
                    <label style={fL}>Scene type presets</label>
                    <div style={{display:"flex",flexDirection:"column",gap:6}}>
                      {[[{key:"SS",label:"Solar System",sub:"All planets + Sun"},{key:"LSN",label:"LSN",sub:"Local Stellar Neighborhood"}],
                        [{key:"ATOMS",label:"Atoms & Molecules",sub:"Coming soon",disabled:true},{key:"MW",label:"Milky Way",sub:"Coming soon",disabled:true}]
                      ].map((row,ri)=>(
                        <div key={ri} style={{display:"flex",gap:6}}>
                          {row.map(({key,label,sub,disabled})=>{
                            const active=(key==="SS"&&passport.purpose&&passport.purpose.includes("solar system"))||(key==="LSN"&&passport.purpose&&passport.purpose.includes("stellar neighborhood"));
                            return (
                              <button key={key} disabled={disabled} onClick={()=>applyPreset(key)} style={{
                                flex:1,minHeight:"56px",height:"auto",padding:"8px 4px",borderRadius:5,cursor:disabled?"default":"pointer",
                                border:"1px solid "+(active?"#c8922a":disabled?"#0e1620":"#1a2838"),
                                background:active?"#1a1200":disabled?"#080a10":"transparent",
                                opacity:disabled?0.35:1,transition:"all .15s",textAlign:"center",
                                display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center"
                              }}>
                                <div style={{color:disabled?"#2a4060":"#c8d8e8",fontSize:13,fontWeight:500}}>{label}</div>
                                <div style={{color:disabled?"#1e3040":"#4a7080",fontSize:12,marginTop:3}}>{sub}</div>
                              </button>
                            );
                          })}
                        </div>
                      ))}
                    </div>
                  </div>
                  <div style={{marginBottom:0}}>
                    <label style={fL}>Sources ({selectedSources.size} selected)</label>
                    <div style={{overflowY:"auto",maxHeight:"35vh",border:"1px solid #111d2b",borderRadius:4}}>
                      {allSources.map(({group,items})=>(
                        <div key={group}>
                          <div style={{padding:"4px 10px",fontSize:11,color:"#4a7888",background:"#0a0d16",letterSpacing:".08em",textTransform:"uppercase",position:"sticky",top:0,zIndex:1}}>{group}</div>
                          {items.map(s=>(
                            <label key={s.id} style={{display:"flex",alignItems:"center",gap:8,padding:"5px 10px",cursor:"pointer",borderBottom:"1px solid #090d16",background:selectedSources.has(s.id)?"#0e1828":"transparent"}}>
                              <input type="checkbox" style={{accentColor:"#c8922a",flexShrink:0}} checked={selectedSources.has(s.id)} onChange={()=>toggleSource(s.id)}/>
                              <span style={{flex:1,color:"#b0c4d4",fontSize:13}}>{s.name}</span>
                              <span style={{color:"#4a7080",fontSize:12,fontFamily:"var(--font-mono)"}}>
                                
                              </span>
                            </label>
                          ))}
                        </div>
                      ))}
                    </div>
                  </div>
                </>);
              })()}
            </div>
          )}
        </div>

        {/* Right panel: JSON */}
        <div style={{flex:1,display:"flex",flexDirection:"column",overflow:"hidden"}}>
          <div style={{padding:"5px 14px",borderBottom:"1px solid #0a1218",display:"flex",justifyContent:"space-between",alignItems:"center",fontSize:"10px",letterSpacing:".1em",textTransform:"uppercase",color:"#c0ccd4",fontWeight:500,flexShrink:0}}>
            <span>Scene passport</span>
            <span style={{color:fc>0?"#7a5010":"#c0ccd4"}}>{fc} field{fc!==1?"s":""} declared</span>
          </div>
          <div style={{flex:1,overflow:"auto",padding:"14px 16px",fontFamily:"var(--font-mono)",fontSize:"13px",lineHeight:1.8}}
            dangerouslySetInnerHTML={{__html:hl(fc>0?JSON.stringify(passport,null,2):"{}")}}/>
          <div style={{padding:"8px 14px",borderTop:"1px solid #0a1218",display:"flex",justifyContent:"flex-end",gap:8,flexShrink:0}}>
            <button className="ab pri" disabled={false}
              onClick={()=>{ const full={...passport,regime:"weak_field_gr_approximation",epoch:"J2000",coordinate_frame:"solar_system_barycentric_cartesian",units:{mass:"kg",distance:"m"},node1:{mode:"explicit_parent",description:"Local Milky Way disk"},datum_architecture:"Single geometric registration datum.",extraction_rungs:RUNGS,claim_status:"diagnostic_candidate_not_observational"}; setLocked(true); onGenerate(full); }}>
              Generate Gravity Map
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

function StageScreen({ passport, onBack }) {
  const containerRef   = useRef(null);
  const rendRef        = useRef(null);
  const camRef         = useRef(null);
  const animRef        = useRef(null);
  const sceneRef       = useRef(null);
  const layerObjsRef   = useRef({});
  const orbitRef       = useRef({ theta:0.4, phi:1.1, radius:120, isDown:false, lastX:0, lastY:0, lastDist:0 });

  const [panelOpen, setPanelOpen]   = useState(false);
  const [geometry,  setGeometry]    = useState(null);
  const [geoStatus, setGeoStatus]   = useState("awaiting");  // awaiting | loading | loaded | error
  const [layers, setLayers] = useState(Object.fromEntries(RUNGS.map(r=>[r,{on:false,opacity:1}])));

  const activeSources = (passport.active_sources||[])
    .map(id=>ALL_SOURCES.find(s=>s.id===id)).filter(Boolean);

  // ── Three.js scene setup ──────────────────────────────────────────────
  useEffect(()=>{
    const el = containerRef.current;
    if (!el) return;
    const W=el.clientWidth, H=el.clientHeight;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x07090d);
    scene.fog = new THREE.FogExp2(0x07090d, 0.0008);
    sceneRef.current = scene;

    const cam = new THREE.PerspectiveCamera(55, W/H, 0.01, 5000);
    camRef.current = cam;

    const ren = new THREE.WebGLRenderer({antialias:true});
    ren.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    ren.setSize(W, H);
    el.appendChild(ren.domElement);
    rendRef.current = ren;

    // Background stars
    const bgGeo = new THREE.BufferGeometry();
    const bgPos = new Float32Array(3000*3);
    for (let i=0;i<3000*3;i++) bgPos[i]=(Math.random()-0.5)*4000;
    bgGeo.setAttribute("position", new THREE.BufferAttribute(bgPos,3));
    scene.add(new THREE.Points(bgGeo, new THREE.PointsMaterial({color:0x8090a0,size:0.25,sizeAttenuation:true})));

    // Source spheres from passport roster
    const hasStellar = activeSources.some(s=>s.dist_pc!==undefined);
    const SCALE = hasStellar ? 20 : 15;
    const positions = activeSources.map((s,i)=>sourcePos(s,i,activeSources.length));
    const solIdx = activeSources.findIndex(s=>s.id==="SOL");
    if (solIdx>=0) positions[solIdx]=[0,0,0];

    activeSources.forEach((s,i)=>{
      const geo = new THREE.SphereGeometry(starSize(s),24,16);
      const col = starColorHex(s.cls);
      const mat = new THREE.MeshStandardMaterial({
        color:col, emissive:col,
        emissiveIntensity:s.id==="SOL"?2.0:0.5,
        roughness:0.5, metalness:0.0,
      });
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(...positions[i]);
      scene.add(mesh);
    });

    scene.add(new THREE.AmbientLight(0x1a2840, 1.2));
    const sunLight = new THREE.PointLight(0xFFE080, 3.0, 800);
    sunLight.position.set(0,0,0);
    scene.add(sunLight);

    // Camera
    const maxD = Math.max(...positions.map(([x,y,z])=>Math.sqrt(x*x+y*y+z*z)), 1);
    const o = orbitRef.current;
    o.radius = maxD * 2.8;
    const updateCam = () => {
      cam.position.set(
        o.radius*Math.sin(o.phi)*Math.cos(o.theta),
        o.radius*Math.cos(o.phi),
        o.radius*Math.sin(o.phi)*Math.sin(o.theta)
      );
      cam.lookAt(0,0,0);
    };
    updateCam();

    // Orbit controls
    const md=e=>{o.isDown=true;o.lastX=e.clientX;o.lastY=e.clientY;};
    const mm=e=>{if(!o.isDown)return;o.theta-=(e.clientX-o.lastX)*0.007;o.phi=Math.max(0.05,Math.min(Math.PI-0.05,o.phi-(e.clientY-o.lastY)*0.007));o.lastX=e.clientX;o.lastY=e.clientY;updateCam();};
    const mu=()=>{o.isDown=false;};
    const mw=e=>{e.preventDefault();o.radius=Math.max(maxD*0.3,Math.min(maxD*8,o.radius*(1+e.deltaY*0.001)));updateCam();};
    const ts=e=>{if(e.touches.length===1){o.isDown=true;o.lastX=e.touches[0].clientX;o.lastY=e.touches[0].clientY;}if(e.touches.length===2)o.lastDist=Math.hypot(e.touches[0].clientX-e.touches[1].clientX,e.touches[0].clientY-e.touches[1].clientY);};
    const tm=e=>{e.preventDefault();if(e.touches.length===1&&o.isDown){o.theta-=(e.touches[0].clientX-o.lastX)*0.007;o.phi=Math.max(0.05,Math.min(Math.PI-0.05,o.phi-(e.touches[0].clientY-o.lastY)*0.007));o.lastX=e.touches[0].clientX;o.lastY=e.touches[0].clientY;updateCam();}if(e.touches.length===2){const d=Math.hypot(e.touches[0].clientX-e.touches[1].clientX,e.touches[0].clientY-e.touches[1].clientY);o.radius=Math.max(maxD*0.3,Math.min(maxD*8,o.radius*(o.lastDist/d)));o.lastDist=d;updateCam();}};
    const te=()=>{o.isDown=false;o.lastDist=0;};
    const me=()=>{document.body.style.overflow='hidden';};
    const ml=()=>{document.body.style.overflow='';};
    ren.domElement.addEventListener("mousedown",md);
    window.addEventListener("mousemove",mm);
    window.addEventListener("mouseup",mu);
    ren.domElement.addEventListener("wheel",mw,{passive:false});
    ren.domElement.addEventListener("touchstart",ts,{passive:true});
    ren.domElement.addEventListener("touchmove",tm,{passive:false});
    ren.domElement.addEventListener("touchend",te);
    el.addEventListener("mouseenter",me);
    el.addEventListener("mouseleave",ml);
    const onResize=()=>{const w=el.clientWidth,h=el.clientHeight;ren.setSize(w,h);cam.aspect=w/h;cam.updateProjectionMatrix();};
    window.addEventListener("resize",onResize);
    const animate=()=>{animRef.current=requestAnimationFrame(animate);ren.render(scene,cam);};
    animate();
    return ()=>{
      cancelAnimationFrame(animRef.current);
      window.removeEventListener("mousemove",mm);
      window.removeEventListener("mouseup",mu);
      window.removeEventListener("resize",onResize);
      el.removeEventListener("mouseenter",me);
      el.removeEventListener("mouseleave",ml);
      document.body.style.overflow='';
      ren.dispose();
      if(el.contains(ren.domElement))el.removeChild(ren.domElement);
    };
  },[]);

  useEffect(()=>{
    if(!rendRef.current||!camRef.current||!containerRef.current)return;
    setTimeout(()=>{
      const w=containerRef.current.clientWidth,h=containerRef.current.clientHeight;
      rendRef.current.setSize(w,h);
      camRef.current.aspect=w/h;
      camRef.current.updateProjectionMatrix();
    },320);
  },[panelOpen]);

  // ── Auto-fetch geometry on stage mount ───────────────────────────────
  useEffect(()=>{
    const url = `https://danski2017.github.io/atlas-solver/geometry/${passport.scene_id}_geometry.json`;
    setGeoStatus("loading");
    fetch(url)
      .then(r => r.json())
      .then(geo => { setGeometry(geo); setGeoStatus("loaded"); })
      .catch(() => setGeoStatus("awaiting"));
  },[]);

  // ── Build Three.js layer objects from geometry ────────────────────────
  useEffect(()=>{
    if (!geometry || !sceneRef.current) return;
    const scene = sceneRef.current;

    // Clear previous layer objects
    Object.values(layerObjsRef.current).flat().forEach(obj => scene.remove(obj));
    layerObjsRef.current = {};

    // Helper: flat position array from nested [[x,y,z],...]
    const flatPos = (arr) => new Float32Array(arr.flat());

    // ── Gravity Boundaries: Apollonius point clouds ───────────────────
    const gbClouds = geometry?.layers?.gravity_boundaries?.clouds || [];
    const gbObjs = [];
    if (gbClouds.length > 0) {
      // Merge all clouds into one Points object for efficiency
      const allPts = gbClouds.flatMap(c => c.positions);
      const geo = new THREE.BufferGeometry();
      geo.setAttribute("position", new THREE.BufferAttribute(flatPos(allPts), 3));
      const mat = new THREE.PointsMaterial({
        color: 0xcc8820, size: 0.18, sizeAttenuation: true,
        transparent: true, opacity: layers.R0_scalar.opacity,
      });
      const pts = new THREE.Points(geo, mat);
      pts.visible = layers.R0_scalar.on;
      scene.add(pts);
      gbObjs.push(pts);
    }
    layerObjsRef.current["R0_scalar"]  = gbObjs;
    layerObjsRef.current["R2_tidal"]   = gbObjs; // same geometry, same toggle

    // ── Star Web: source-context boundary clouds ──────────────────────
    const swClouds = geometry?.layers?.star_web?.clouds || [];
    const swObjs = [];
    if (swClouds.length > 0) {
      const allPts = swClouds.flatMap(c => c.positions);
      const geo = new THREE.BufferGeometry();
      geo.setAttribute("position", new THREE.BufferAttribute(flatPos(allPts), 3));
      const mat = new THREE.PointsMaterial({
        color: 0x40c880, size: 0.22, sizeAttenuation: true,
        transparent: true, opacity: layers.SS_bones.opacity,
      });
      const pts = new THREE.Points(geo, mat);
      pts.visible = layers.SS_bones.on;
      scene.add(pts);
      swObjs.push(pts);
    }
    layerObjsRef.current["SS_bones"] = swObjs;

    // ── Orientation Shifts: eigenvector tick segments ─────────────────
    const segs = geometry?.layers?.orientation_shifts?.data?.segments || [];
    const osObjs = [];
    if (segs.length > 0) {
      const posArr = [];
      const colArr = [];
      for (const seg of segs) {
        posArr.push(...seg.p0, ...seg.p1);
        colArr.push(...seg.color, ...seg.color);
      }
      const geo = new THREE.BufferGeometry();
      geo.setAttribute("position", new THREE.BufferAttribute(new Float32Array(posArr), 3));
      geo.setAttribute("color",    new THREE.BufferAttribute(new Float32Array(colArr),  3));
      const mat = new THREE.LineBasicMaterial({
        vertexColors: true, transparent: true,
        opacity: layers.eigenframe_handoff.opacity,
      });
      const lines = new THREE.LineSegments(geo, mat);
      lines.visible = layers.eigenframe_handoff.on;
      scene.add(lines);
      osObjs.push(lines);
    }
    layerObjsRef.current["eigenframe_handoff"] = osObjs;
    layerObjsRef.current["witness_skeleton"]   = osObjs; // share toggle

  }, [geometry]);

  // ── Sync layer visibility + opacity to Three.js objects ──────────────
  useEffect(()=>{
    Object.entries(layers).forEach(([key, {on, opacity}]) => {
      (layerObjsRef.current[key] || []).forEach(obj => {
        obj.visible = on;
        if (obj.material) obj.material.opacity = opacity;
      });
    });
  }, [layers]);

  // ── Render ────────────────────────────────────────────────────────────
  return (
    <div style={{position:"relative",width:"100%",height:"100%",background:"#07090d",overflow:"hidden",display:"flex"}}>
      <style>{`
        input[type=range]{accent-color:#c8922a;width:100%;margin:4px 0;}
        .tog{width:34px;height:19px;border-radius:10px;cursor:pointer;position:relative;transition:background .2s;flex-shrink:0;border:none;}
        .tog-knob{position:absolute;top:2px;width:15px;height:15px;border-radius:50%;background:#c0ccd4;transition:left .2s;}
      `}</style>

      <div ref={containerRef} style={{flex:1,height:"100%",transition:"flex .3s ease",overflow:"hidden"}}/>

      {/* Slide-in panel */}
      <div style={{
        width:panelOpen?"25%":"0",minWidth:panelOpen?"220px":"0",height:"100%",
        background:"rgba(7,9,13,0.97)",borderLeft:panelOpen?"1px solid #111d2b":"none",
        overflow:"hidden",transition:"width .3s ease, min-width .3s ease",
        display:"flex",flexDirection:"column",flexShrink:0,
      }}>
        <div style={{padding:"56px 14px 14px",overflowY:"auto",flex:1}}>

          {/* Scene info */}
          <div style={{marginBottom:18,paddingBottom:14,borderBottom:"1px solid #111d2b"}}>
            <div style={{color:"#c8922a",fontSize:11,fontWeight:500,letterSpacing:".1em",textTransform:"uppercase",marginBottom:6}}>Scene</div>
            <div style={{color:"#c0ccd4",fontSize:13,wordBreak:"break-all"}}>{passport.scene_id||"unnamed"}</div>
            <div style={{color:"#5a8090",fontSize:12,marginTop:4}}>{activeSources.length} sources</div>
          </div>

          {/* Geometry loader */}
          <div style={{marginBottom:18,paddingBottom:14,borderBottom:"1px solid #111d2b"}}>
            <div style={{color:"#c8922a",fontSize:11,fontWeight:500,letterSpacing:".1em",textTransform:"uppercase",marginBottom:8}}>Geometry</div>
            <div style={{fontSize:12,color:
              geoStatus==="loaded"  ? "#3a9060" :
              geoStatus==="loading" ? "#c8922a" :
              geoStatus==="error"   ? "#904040" : "#4a6878"
            }}>
              {geoStatus==="loaded"  ? `Loaded — ${geometry?.n_sources||"?"} sources` :
               geoStatus==="loading" ? "Loading..." :
               geoStatus==="error"   ? "Error loading" :
               "Awaiting geometry"}
            </div>
          </div>

          {/* Layer toggles */}
          <div style={{color:"#c8922a",fontSize:11,fontWeight:500,letterSpacing:".1em",textTransform:"uppercase",marginBottom:12}}>Layers</div>
          {RUNGS.map(key=>(
            <div key={key} style={{marginBottom:16}}>
              <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",gap:8,marginBottom:4}}>
                <div>
                  <div style={{color:layers[key].on?"#c8d8e8":"#4a6878",fontSize:13,fontWeight:500,lineHeight:1.3}}>{RUNG_INFO[key].label}</div>
                  <div style={{fontSize:11,marginTop:2,color:
                    geoStatus==="loaded" && (layerObjsRef.current[key]||[]).length>0
                      ? "#2a6040" : "#1e3040"
                  }}>
                    {geoStatus==="loaded" && (layerObjsRef.current[key]||[]).length>0
                      ? "ready" : "awaiting geometry"}
                  </div>
                </div>
                <button className="tog"
                  style={{background:layers[key].on?"#c8922a":"#1a2838"}}
                  onClick={()=>setLayers(l=>({...l,[key]:{...l[key],on:!l[key].on}}))}>
                  <div className="tog-knob" style={{left:layers[key].on?17:2}}/>
                </button>
              </div>
              {layers[key].on&&<input type="range" min={0} max={100}
                value={Math.round(layers[key].opacity*100)}
                onChange={e=>setLayers(l=>({...l,[key]:{...l[key],opacity:e.target.value/100}}))}/>}
            </div>
          ))}

          {/* Back */}
          <button onClick={onBack} style={{marginTop:8,width:"100%",padding:"9px 0",background:"transparent",border:"1px solid #1a2838",color:"#c0ccd4",fontSize:13,fontFamily:"var(--font-sans)",borderRadius:5,cursor:"pointer"}}>
            ← Passport
          </button>
        </div>
      </div>

      {/* Toggle button */}
      <button onClick={()=>setPanelOpen(p=>!p)} style={{
        position:"absolute",top:14,right:14,zIndex:200,
        background:"rgba(8,10,14,0.88)",border:"1px solid #1a2838",
        color:"#c0ccd4",fontFamily:"var(--font-sans)",fontSize:13,fontWeight:500,
        padding:"8px 16px",borderRadius:5,cursor:"pointer",
        backdropFilter:"blur(8px)",transition:"all .15s"
      }}>
        {panelOpen?"Hide":"Controls"}
      </button>
    </div>
  );
}

export default function AtlasInstrument() {
  const [phase, setPhase] = useState("passport");
  const [passport, setPassport] = useState({});
  const [opacity, setOpacity] = useState(1);

  const fadeTo = (fn) => {
    setOpacity(0);
    setTimeout(()=>{ fn(); setOpacity(1); }, 380);
  };

  return (
    <div style={{width:"100%",height:"100%",overflow:"hidden",opacity,transition:"opacity 0.38s ease"}}>
      {phase==="passport"
        ? <PassportScreen onGenerate={p=>fadeTo(()=>{ setPassport(p); setPhase("stage"); })}/>
        : <StageScreen passport={passport} onBack={()=>fadeTo(()=>setPhase("passport"))}/> }
    </div>
  );
}
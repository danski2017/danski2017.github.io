import { useState, useRef, useEffect } from "react";
import * as THREE from 'three';

// ── ROSTERS ──────────────────────────────────────────────────────────────────

const SOLAR_SYSTEM = [
  { id:"SOL",     name:"Sun",     cls:"star_G2",      mass_msun:1.0,      dist_au:0    },
  { id:"MERCURY", name:"Mercury", cls:"planet",       mass_msun:1.65e-7,  dist_au:0.39 },
  { id:"VENUS",   name:"Venus",   cls:"planet",       mass_msun:2.45e-6,  dist_au:0.72 },
  { id:"EARTH",   name:"Earth",   cls:"planet",       mass_msun:3.00e-6,  dist_au:1.00 },
  { id:"MOON",    name:"Moon",    cls:"moon",         mass_msun:3.69e-8,  dist_au:1.003},
  { id:"MARS",    name:"Mars",    cls:"planet",       mass_msun:3.23e-7,  dist_au:1.52 },
  { id:"JUPITER", name:"Jupiter", cls:"planet",       mass_msun:9.55e-4,  dist_au:5.20 },
  { id:"SATURN",  name:"Saturn",  cls:"planet",       mass_msun:2.86e-4,  dist_au:9.58 },
  { id:"URANUS",  name:"Uranus",  cls:"planet",       mass_msun:4.37e-5,  dist_au:19.2 },
  { id:"NEPTUNE", name:"Neptune", cls:"planet",       mass_msun:5.15e-5,  dist_au:30.1 },
  { id:"PLUTO",   name:"Pluto",   cls:"dwarf_planet", mass_msun:6.6e-9,   dist_au:39.5 },
];

const GAIA_NEIGHBORS = [
  { id:"PROXIMA_CEN",   name:"Proxima Centauri",  cls:"M-dwarf",    mass_msun:0.1221, dist_pc:1.295 },
  { id:"ALPHA_CEN_A",   name:"Alpha Centauri A",  cls:"G-star",     mass_msun:1.1,    dist_pc:1.338 },
  { id:"ALPHA_CEN_B",   name:"Alpha Centauri B",  cls:"K-star",     mass_msun:0.907,  dist_pc:1.338 },
  { id:"BARNARDS",      name:"Barnard's Star",    cls:"M-dwarf",    mass_msun:0.144,  dist_pc:1.828 },
  { id:"LUHMAN16A",     name:"Luhman 16 A",       cls:"brown_dwarf",mass_msun:0.032,  dist_pc:1.998 },
  { id:"LUHMAN16B",     name:"Luhman 16 B",       cls:"brown_dwarf",mass_msun:0.027,  dist_pc:1.998 },
  { id:"WISE0855",      name:"WISE 0855-0714",    cls:"brown_dwarf",mass_msun:0.008,  dist_pc:2.231 },
  { id:"WOLF359",       name:"Wolf 359",          cls:"M-dwarf",    mass_msun:0.09,   dist_pc:2.394 },
  { id:"LALANDE21185",  name:"Lalande 21185",     cls:"M-dwarf",    mass_msun:0.386,  dist_pc:2.547 },
  { id:"SIRIUS_A",      name:"Sirius A",          cls:"A-star",     mass_msun:2.063,  dist_pc:2.637 },
  { id:"SIRIUS_B",      name:"Sirius B",          cls:"white_dwarf",mass_msun:1.018,  dist_pc:2.637 },
  { id:"BL_CETI",       name:"BL Ceti",           cls:"M-dwarf",    mass_msun:0.102,  dist_pc:2.68  },
  { id:"UV_CETI",       name:"UV Ceti",           cls:"M-dwarf",    mass_msun:0.1,    dist_pc:2.68  },
  { id:"ROSS154",       name:"Ross 154",          cls:"M-dwarf",    mass_msun:0.17,   dist_pc:2.976 },
  { id:"ROSS248",       name:"Ross 248",          cls:"M-dwarf",    mass_msun:0.136,  dist_pc:3.162 },
  { id:"EPS_ERI",       name:"Epsilon Eridani",   cls:"K-star",     mass_msun:0.832,  dist_pc:3.218 },
  { id:"LACAILLE9352",  name:"Lacaille 9352",     cls:"M-dwarf",    mass_msun:0.503,  dist_pc:3.289 },
  { id:"ROSS128",       name:"Ross 128",          cls:"M-dwarf",    mass_msun:0.168,  dist_pc:3.374 },
  { id:"EZ_AQR_A",      name:"EZ Aquarii A",      cls:"M-dwarf",    mass_msun:0.11,   dist_pc:3.452 },
  { id:"61CYGNI_A",     name:"61 Cygni A",        cls:"K-star",     mass_msun:0.708,  dist_pc:3.497 },
  { id:"61CYGNI_B",     name:"61 Cygni B",        cls:"K-star",     mass_msun:0.63,   dist_pc:3.497 },
  { id:"STRUVE2398A",   name:"Struve 2398 A",     cls:"M-dwarf",    mass_msun:0.342,  dist_pc:3.517 },
  { id:"STRUVE2398B",   name:"Struve 2398 B",     cls:"M-dwarf",    mass_msun:0.248,  dist_pc:3.517 },
  { id:"GROOMBRIDGE34A",name:"Groombridge 34 A",  cls:"M-dwarf",    mass_msun:0.38,   dist_pc:3.561 },
  { id:"GROOMBRIDGE34B",name:"Groombridge 34 B",  cls:"M-dwarf",    mass_msun:0.158,  dist_pc:3.561 },
  { id:"DX_CANCRI",     name:"DX Cancri",         cls:"M-dwarf",    mass_msun:0.09,   dist_pc:3.582 },
  { id:"EPS_INDI_A",    name:"Epsilon Indi A",    cls:"K-star",     mass_msun:0.762,  dist_pc:3.622 },
  { id:"EPS_INDI_BA",   name:"Epsilon Indi Ba",   cls:"brown_dwarf",mass_msun:0.065,  dist_pc:3.622 },
  { id:"EPS_INDI_BB",   name:"Epsilon Indi Bb",   cls:"brown_dwarf",mass_msun:0.053,  dist_pc:3.622 },
  { id:"TAU_CETI",      name:"Tau Ceti",          cls:"G-star",     mass_msun:0.783,  dist_pc:3.65  },
  { id:"GJ1061",        name:"GJ 1061",           cls:"M-dwarf",    mass_msun:0.113,  dist_pc:3.674 },
  { id:"YZ_CETI",       name:"YZ Ceti",           cls:"M-dwarf",    mass_msun:0.13,   dist_pc:3.722 },
  { id:"LUYTEN_STAR",   name:"Luyten's Star",     cls:"M-dwarf",    mass_msun:0.26,   dist_pc:3.785 },
  { id:"TEEGARDEN",     name:"Teegarden's Star",  cls:"M-dwarf",    mass_msun:0.089,  dist_pc:3.831 },
  { id:"SCR1845",       name:"SCR 1845-6357 A",   cls:"M-dwarf",    mass_msun:0.092,  dist_pc:3.876 },
  { id:"KAPTEYN",       name:"Kapteyn's Star",    cls:"M-dwarf",    mass_msun:0.274,  dist_pc:3.934 },
  { id:"LACAILLE8760",  name:"Lacaille 8760",     cls:"M-dwarf",    mass_msun:0.601,  dist_pc:3.969 },
  { id:"KRUGER60A",     name:"Kruger 60 A",       cls:"M-dwarf",    mass_msun:0.271,  dist_pc:4.01  },
  { id:"KRUGER60B",     name:"Kruger 60 B",       cls:"M-dwarf",    mass_msun:0.176,  dist_pc:4.01  },
  { id:"ROSS614A",      name:"Ross 614 A",        cls:"M-dwarf",    mass_msun:0.222,  dist_pc:4.13  },
  { id:"VAN_MAANEN",    name:"Van Maanen's Star", cls:"white_dwarf",mass_msun:0.67,   dist_pc:4.334 },
  { id:"GLIESE1",       name:"Gliese 1",          cls:"M-dwarf",    mass_msun:0.38,   dist_pc:4.345 },
  { id:"WOLF424A",      name:"Wolf 424 A",        cls:"M-dwarf",    mass_msun:0.14,   dist_pc:4.392 },
  { id:"TZ_ARIETIS",    name:"TZ Arietis",        cls:"M-dwarf",    mass_msun:0.15,   dist_pc:4.461 },
  { id:"GJ687",         name:"GJ 687",            cls:"M-dwarf",    mass_msun:0.413,  dist_pc:4.53  },
  { id:"GJ674",         name:"GJ 674",            cls:"M-dwarf",    mass_msun:0.35,   dist_pc:4.547 },
  { id:"GJ440",         name:"GJ 440",            cls:"white_dwarf",mass_msun:0.55,   dist_pc:4.626 },
  { id:"GJ1002",        name:"GJ 1002",           cls:"M-dwarf",    mass_msun:0.117,  dist_pc:4.844 },
  { id:"GJ412A",        name:"GJ 412 A",          cls:"M-dwarf",    mass_msun:0.396,  dist_pc:4.854 },
];

const ALL_SOURCES = [...SOLAR_SYSTEM, ...GAIA_NEIGHBORS];

// Approximate J2000 mean longitudes (radians) for ecliptic placement
const ORBITAL_ANGLES = {
  SOL:0, MERCURY:4.40, VENUS:3.18, EARTH:1.75, MOON:1.78,
  MARS:5.87, JUPITER:0.60, SATURN:1.98, URANUS:5.53, NEPTUNE:5.31, PLUTO:3.91
};

// ── VISUAL UTILITIES ─────────────────────────────────────────────────────────

const slugify = s => s.toLowerCase().replace(/[^a-z0-9]+/g,"_").replace(/^_|_$/g,"");

const fibSphere = (i,n) => {
  const phi = Math.acos(1-2*(i+0.5)/n);
  const theta = Math.PI*(1+Math.sqrt(5))*i;
  return [Math.sin(phi)*Math.cos(theta), Math.cos(phi), Math.sin(phi)*Math.sin(theta)];
};

const starColor = cls => ({
  star_G2:"#FFE060","G-star":"#FFD050","K-star":"#FF9040","M-dwarf":"#FF5030",
  "A-star":"#C0E0FF",white_dwarf:"#90B0FF",brown_dwarf:"#5A2A18",
  planet:"#4080C0",moon:"#909090",dwarf_planet:"#807060",
})[cls]||"#CCCCCC";

const starColorHex = cls => parseInt(starColor(cls).replace('#',''),16);

// Real radii in AU (exaggerated ~15× so they're visible dots, not hiding GCS)
const AU_RADII = {
  SOL:0.07, MERCURY:0.004, VENUS:0.006, EARTH:0.006, MOON:0.002,
  MARS:0.005, JUPITER:0.02, SATURN:0.018, URANUS:0.012, NEPTUNE:0.012, PLUTO:0.002
};
const starSize = (s, scaleAU) => {
  if(scaleAU) return AU_RADII[s.id]||0.005;
  // pc-scale scene (stellar neighborhood)
  if(s.id==='SOL') return 1.0;
  return Math.max(0.22, Math.min(1.4, Math.pow(s.mass_msun, 0.35)*1.1));
};

const sourcePos = (s,i,n) => {
  if(s.dist_pc!==undefined){
    // Stellar/pc-scale: Fibonacci sphere
    const [fx,fy,fz] = fibSphere(i,n);
    return [fx*s.dist_pc*20, fy*s.dist_pc*20, fz*s.dist_pc*20];
  }
  // AU-scale: ecliptic plane placement
  const d = s.dist_au||0;
  if(d===0) return [0,0,0];
  const angle = ORBITAL_ANGLES[s.id]||0;
  const yOff = s.id==='PLUTO' ? d*0.15 : 0; // Pluto ~17° inclination
  return [d*Math.cos(angle), yOff, d*Math.sin(angle)];
};

const SCENE_PRESETS = {
  SS:  { purpose:"Gravitational geometry and tidal structure of the solar system",
         sources: new Set(SOLAR_SYSTEM.map(s=>s.id)) },
  LSN: { purpose:"Gravitational geometry and tidal structure of the local stellar neighborhood",
         sources: new Set(["SOL",...GAIA_NEIGHBORS.map(s=>s.id)]) },
};

// ── COMPUTE ENGINE ───────────────────────────────────────────────────────────
// C_VIS is a toy speed-of-light that makes 1PN effects pedagogically visible.
// Physical GR uses c=3e8 m/s; here we use a small value so the cross-term
// correction produces a visible GCS boundary shift at solar-system scales.

const G=1.0, SOFT=0.001, C_VIS=5.0;

const vadd=(a,b)=>[a[0]+b[0],a[1]+b[1],a[2]+b[2]];
const vsub=(a,b)=>[a[0]-b[0],a[1]-b[1],a[2]-b[2]];
const vscale=(a,s)=>[a[0]*s,a[1]*s,a[2]*s];
const vnorm=a=>Math.sqrt(a[0]**2+a[1]**2+a[2]**2);
const vnormalize=a=>{const n=vnorm(a);return n>1e-12?vscale(a,1/n):[1,0,0];};
const vdot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
const vcross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];

const mzero=()=>[[0,0,0],[0,0,0],[0,0,0]];
const madd=(A,B)=>A.map((r,i)=>r.map((v,j)=>v+B[i][j]));
const mscale=(A,s)=>A.map(r=>r.map(v=>v*s));
const mfrob=A=>{let s=0;A.forEach(r=>r.forEach(v=>s+=v*v));return Math.sqrt(s);};
const outer3=(a,b)=>[[a[0]*b[0],a[0]*b[1],a[0]*b[2]],[a[1]*b[0],a[1]*b[1],a[1]*b[2]],[a[2]*b[0],a[2]*b[1],a[2]*b[2]]];
const mvmul=(M,v)=>M.map(r=>r[0]*v[0]+r[1]*v[1]+r[2]*v[2]);

// R2: linearized tidal tensor, single source
const tidalSingle=(mass,srcPos,pt)=>{
  const r=vsub(pt,srcPos),d=Math.max(vnorm(r),SOFT),n=vscale(r,1/d),p=G*mass/d**3;
  return Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>p*(3*n[i]*n[j]-(i===j?1:0))));
};

// R2: scene tidal (superposed)
const tidalScene=(srcs,pt,excl)=>srcs.reduce((E,s)=>s.id===excl?E:madd(E,tidalSingle(s.mass,s.pos,pt)),mzero());

// R0: Newtonian potential (positive, U=GM/r)
const uVal=(m,sp,x)=>G*m/Math.max(vnorm(vsub(x,sp)),SOFT);
const gradU=(m,sp,x)=>{const r=vsub(x,sp),d=Math.max(vnorm(r),SOFT);return vscale(vscale(r,1/d),-G*m/d**2);};
const uTotal=(srcs,x,excl)=>srcs.reduce((a,s)=>s.id===excl?a:a+uVal(s.mass,s.pos,x),0);
const gradUTotal=(srcs,x,excl)=>srcs.reduce((a,s)=>{
  if(s.id===excl)return a;const g=gradU(s.mass,s.pos,x);return[a[0]+g[0],a[1]+g[1],a[2]+g[2]];
},[0,0,0]);

// R5: 1PN-corrected tidal tensor (GPT/lab-verified formula)
// E_ij^1PN = U_,ij − (1/c²)[2U·U_,ij + 3∇U_i·∇U_j − δ_ij|∇U|²]
const e1pnFull=(srcs,x)=>{
  const U=uTotal(srcs,x),gU=gradUTotal(srcs,x),En=tidalScene(srcs,x),gU2=vdot(gU,gU);
  const o=outer3(gU,gU);
  const corr=Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>
    -(1/C_VIS**2)*(2*U*En[i][j]+3*o[i][j]-(i===j?1:0)*gU2)));
  return madd(En,corr);
};

// Power iteration: dominant eigenvector of a symmetric 3×3 matrix
const dominantEigen=(M,iters=20)=>{
  let v=vnormalize([1,0.3,0.1]);
  for(let k=0;k<iters;k++){const w=mvmul(M,v);const n=vnorm(w);if(n<1e-14)break;v=vscale(w,1/n);}
  const Mv=mvmul(M,v);return{vec:v,val:vdot(v,Mv)};
};

// Fibonacci sphere ray directions
const fibRays=n=>{
  const phi=(1+Math.sqrt(5))/2;
  return Array.from({length:n},(_,i)=>{
    const t=2*Math.PI*i/phi,cp=1-2*(i+0.5)/n,sp=Math.sqrt(1-cp**2);
    return[sp*Math.cos(t),sp*Math.sin(t),cp];
  });
};

// Log-spaced radial grid (catches inner crossings for mass-asymmetric pairs)
const logGrid=(rmax,n)=>{const rm=0.001*rmax;return Array.from({length:n},(_,i)=>rm*Math.pow(rmax/rm,i/(n-1)));};

// Apollonius-based estimate of max expected GCS radius for a source
const gcsRmax=(srcs,sid)=>{
  const src=srcs.find(s=>s.id===sid);
  let rmax=0;
  for(const o of srcs){
    if(o.id===sid)continue;
    const d=vnorm(vsub(o.pos,src.pos));if(d<1e-8)continue;
    const ratio=Math.pow(Math.max(src.mass,1e-30)/Math.max(o.mass,1e-30),1/3);
    rmax=Math.max(rmax,d*ratio/(1+ratio)*1.1);
  }
  return rmax||0.5;
};

// Extract GCS crossing points for one source (R2 or R5 operator)
const extractGCS=(srcs,sid,rays,nRadial,use1pn)=>{
  const src=srcs.find(s=>s.id===sid);
  const rmax=gcsRmax(srcs,sid),radii=logGrid(rmax,nRadial),pts=[];
  for(const dhat of rays){
    let prev=null;
    for(let ri=0;ri<radii.length;ri++){
      const r=radii[ri],p=vadd(src.pos,vscale(dhat,r));
      const Es=tidalSingle(src.mass,src.pos,p);
      const Ec=use1pn?madd(e1pnFull(srcs,p),mscale(Es,-1)):tidalScene(srcs,p,sid);
      const res=mfrob(Es)-mfrob(Ec);
      if(prev!==null&&prev*res<0){
        const r0=radii[ri-1],t=prev/(prev-res),rc=r0+t*(r-r0);
        pts.push(vadd(src.pos,vscale(dhat,rc)));
      }
      prev=res;
    }
  }
  return pts;
};

// Eigenframe sample points around a source (dominant eigenvector of E_ij)
const extractEigenframe=(srcs,sid,nPts,radius,use1pn)=>{
  const src=srcs.find(s=>s.id===sid);
  return fibRays(nPts).map(d=>{
    const p=vadd(src.pos,vscale(d,radius));
    const E=use1pn?e1pnFull(srcs,p):tidalScene(srcs,p);
    const{vec,val}=dominantEigen(E);
    return{pos:p,dir:vec,val};
  });
};

// Convert passport active_sources to compute format with 3D positions
const passportToComputeSources=actives=>{
  const n=actives.length;
  const positions=actives.map((s,i)=>sourcePos(s,i,n));
  const solIdx=actives.findIndex(s=>s.id==='SOL');
  if(solIdx>=0)positions[solIdx]=[0,0,0];
  // Moon relative to Earth (0.00257 AU = ~384,400 km)
  const earthIdx=actives.findIndex(s=>s.id==='EARTH');
  const moonIdx=actives.findIndex(s=>s.id==='MOON');
  if(earthIdx>=0&&moonIdx>=0){
    const ma=ORBITAL_ANGLES['MOON']||0;
    positions[moonIdx]=[positions[earthIdx][0]+0.00257*Math.cos(ma),positions[earthIdx][1],positions[earthIdx][2]+0.00257*Math.sin(ma)];
  }
  return actives.map((s,i)=>({id:s.id,name:s.name,cls:s.cls,mass:s.mass_msun,pos:positions[i],vel:[0,0,0]}));
};

// Assign sub-circular orbit velocities around dominant mass
const circularOrbits=srcs=>{
  const anchor=srcs.reduce((a,b)=>b.mass>a.mass?b:a);
  return srcs.map(s=>{
    if(s.id===anchor.id)return{...s,vel:[0,0,0]};
    const r=vsub(s.pos,anchor.pos),d=vnorm(r);
    if(d<1e-8)return{...s,vel:[0,0,0]};
    const rhat=vscale(r,1/d),vcirc=Math.sqrt(G*anchor.mass/d)*0.82;
    const up=[0,1,0],t1=vnormalize(vcross(rhat,Math.abs(vdot(rhat,up))>0.9?[1,0,0]:up));
    return{...s,vel:vscale(vcross(rhat,t1),vcirc)};
  });
};

// N-body leapfrog step
const nbodyAccel=srcs=>srcs.map(si=>srcs.reduce((a,sj)=>{
  if(sj.id===si.id)return a;
  const r=vsub(sj.pos,si.pos),d=vnorm(r);
  return vadd(a,vscale(r,G*sj.mass/(d**2+SOFT**2)**1.5));
},[0,0,0]));

const leapfrogStep=(srcs,dt)=>{
  const a1=nbodyAccel(srcs);
  const s1=srcs.map((s,i)=>({...s,vel:vadd(s.vel,vscale(a1[i],0.5*dt))}));
  const s2=s1.map(s=>({...s,pos:vadd(s.pos,vscale(s.vel,dt))}));
  const a2=nbodyAccel(s2);
  return s2.map((s,i)=>({...s,vel:vadd(s.vel,vscale(a2[i],0.5*dt))}));
};

// ── AI PASSPORT ──────────────────────────────────────────────────────────────

const RUNGS_LIST = ["R0_scalar","R2_tidal","SS_bones","witness_skeleton","eigenframe_handoff"];

const SYSTEM_PROMPT = `You are the Atlas Passport Builder AI. Guide researchers through declaring gravitational scene passports via natural conversation.

ATLAS DOCTRINE: Sources contribute. Datums interrogate. Ledger remembers. No modified GR. claim_status always: diagnostic_candidate_not_observational.

ROSTER: Solar system (SOL, MERCURY, VENUS, EARTH, MOON, MARS, JUPITER, SATURN, URANUS, NEPTUNE, PLUTO) + 49 Gaia stellar neighbors to 4.9 pc.

PASSPORT FIELDS: scene_id (snake_case_v0_1), purpose, regime (weak_field_gr_approximation), epoch (J2000), coordinate_frame (solar_system_barycentric_cartesian), units {mass:kg, distance:m}, node1 {mode:explicit_parent, description}, active_sources (array of exact roster IDs), datum_architecture, extraction_rungs (always full suite), claim_status.

- Be conversational, plain language, one question at a time.
- Always set extraction_rungs to full suite, never ask the user.
- Use exact roster IDs in active_sources.
- End messages with cumulative <passport_update>{ ... }</passport_update>
- When complete say: Your passport is ready to lock.`;

const WELCOME = `Atlas Passport Builder online.\n\nRoster loaded: 11 solar system bodies + 49 Gaia stellar neighbors to 4.9 pc.\n\nDescribe the scene you want to study.`;

// ── PASSPORT SCREEN ──────────────────────────────────────────────────────────

function PassportScreen({ onGenerate }) {
  const [messages, setMessages] = useState([{role:"assistant",content:WELCOME}]);
  const [passport, setPassport] = useState({});
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [locked, setLocked] = useState(false);
  const [ready, setReady] = useState(false);
  const [mode, setMode] = useState("manual");
  const [renderMode, setRenderMode] = useState("static");
  const [selectedSources, setSelectedSources] = useState(new Set());
  const bottomRef = useRef(null);

  useEffect(()=>{bottomRef.current?.scrollIntoView({behavior:"smooth"});},[messages,loading]);

  const updateManual=(field,val)=>setPassport(p=>({...p,[field]:val}));
  const toggleSource=id=>{
    setSelectedSources(prev=>{
      const next=new Set(prev);
      next.has(id)?next.delete(id):next.add(id);
      setPassport(p=>({...p,active_sources:[...next]}));
      return next;
    });
  };
  const applyPreset=key=>{
    const p=SCENE_PRESETS[key];if(!p)return;
    setSelectedSources(p.sources);
    setPassport(prev=>({...prev,purpose:p.purpose,active_sources:[...p.sources]}));
  };
  const allSources=[
    {group:"Solar System",items:SOLAR_SYSTEM},
    {group:"Stellar Neighbors",items:GAIA_NEIGHBORS.slice().sort((a,b)=>a.dist_pc-b.dist_pc)},
  ];

  const parseUpdate=t=>{const m=t.match(/<passport_update>([\s\S]*?)<\/passport_update>/);if(m){try{return JSON.parse(m[1].trim())}catch{}}return null;};
  const stripUpdate=t=>t.replace(/<passport_update>[\s\S]*?<\/passport_update>/g,"").trim();

  const sendAI=async()=>{
    if(!input.trim()||loading||locked)return;
    const um={role:"user",content:input.trim()};
    const hist=[...messages,um];
    setMessages(hist);setInput("");setLoading(true);
    try{
      const res=await fetch("https://api.anthropic.com/v1/messages",{
        method:"POST",headers:{"Content-Type":"application/json","anthropic-version":"2023-06-01","x-api-key":""},
        body:JSON.stringify({model:"claude-sonnet-4-20250514",max_tokens:1000,system:SYSTEM_PROMPT,messages:hist.map(m=>({role:m.role,content:m.content}))})
      });
      const d=await res.json();
      const raw=d.content?.[0]?.text||"No response.";
      const upd=parseUpdate(raw);if(upd)setPassport(p=>({...p,...upd}));
      const txt=stripUpdate(raw);
      if(txt.includes("Your passport is ready to lock."))setReady(true);
      setMessages(p=>[...p,{role:"assistant",content:txt}]);
    }catch{setMessages(p=>[...p,{role:"assistant",content:"Connection error."}]);}
    finally{setLoading(false);}
  };

  const onKey=e=>{if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();sendAI();}};
  const fc=Object.keys(passport).length;

  const hl=json=>{
    if(!json||json==="{}") return '<span style="color:#1e3452;font-style:italic">// awaiting declarations...</span>';
    return json.replace(/("(?:\\u[a-fA-F0-9]{4}|\\[^u]|[^\\"])*"(?:\s*:)?|\b(?:true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)/g,m=>{
      if(/^"./.test(m)&&/:$/.test(m))return`<span style="color:#4a9aba">${m}</span>`;
      if(/^"/.test(m))return`<span style="color:#a0b4c4">${m}</span>`;
      if(/true|false/.test(m))return`<span style="color:#a05080">${m}</span>`;
      if(/null/.test(m))return`<span style="color:#2a4a60">${m}</span>`;
      return`<span style="color:#b07820">${m}</span>`;
    });
  };

  const fL={display:"block",fontSize:11,color:"#c0ccd4",marginBottom:4,fontWeight:500};
  const fI={width:"100%",background:"#0b0d14",border:"1px solid #14202e",color:"#a0b8cc",fontFamily:"var(--font-sans)",fontSize:12,padding:"4px 8px",borderRadius:4,outline:"none",boxSizing:"border-box"};

  const doGenerate=()=>{
    const full={...passport,render_mode:renderMode,regime:"weak_field_gr_approximation",epoch:"J2000",
      coordinate_frame:"solar_system_barycentric_cartesian",
      units:{mass:"kg",distance:"m"},node1:{mode:"explicit_parent",description:"Local Milky Way disk"},
      datum_architecture:"Single geometric registration datum.",
      extraction_rungs:RUNGS_LIST,claim_status:"diagnostic_candidate_not_observational"};
    setLocked(true);onGenerate(full);
  };

  return (
    <div style={{display:"flex",flexDirection:"column",height:"100%",fontFamily:"var(--font-sans)",fontSize:"11px",background:"#07090d",color:"#a0b8cc"}}>
      <style>{`
        @keyframes blink{0%,80%,100%{opacity:.2;transform:scale(.7)}40%{opacity:1;transform:scale(1)}}
        .dot{display:inline-block;width:4px;height:4px;border-radius:50%;background:#a07018;animation:blink 1.2s ease-in-out infinite;margin:0 2px}
        .dot:nth-child(2){animation-delay:.2s}.dot:nth-child(3){animation-delay:.4s}
        .tinp{width:100%;background:#0b0d14;border:1px solid #14202e;color:#a0b8cc;font-family:var(--font-sans);font-size:11px;padding:5px 8px;border-radius:4px;resize:none;outline:none;line-height:1.5;box-sizing:border-box}
        .tinp:focus{border-color:#6a4410}.tinp::placeholder{color:#2a4060}.tinp:disabled{opacity:.3;cursor:not-allowed}
        .ab{font-family:var(--font-sans);font-size:11px;letter-spacing:.06em;font-weight:500;padding:4px 10px;border-radius:4px;cursor:pointer;transition:all .15s;white-space:nowrap}
        .pri{background:#7a4e10;border:1px solid #7a4e10;color:#ddb870}.pri:hover{background:#8e5c18}
        .pri:disabled{background:#0d1520;border-color:#111e2c;color:#182840;cursor:not-allowed}
        .gho{background:transparent;border:1px solid #14202e;color:#c0ccd4}.gho:hover{border-color:#2a4060;color:#7aaccc;background:#090d14}
        .gho:disabled{opacity:.25;cursor:not-allowed;pointer-events:none}
        ::-webkit-scrollbar{width:3px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:#14202e;border-radius:2px}
      `}</style>

      {/* Header */}
      <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",padding:"5px 12px",borderBottom:"1px solid #0c1620",background:"#080a10",flexShrink:0}}>
        <span style={{fontSize:"15px",fontWeight:500,letterSpacing:".14em",color:"#a07018"}}>ATLAS</span>
        <div style={{display:"flex",gap:"6px",alignItems:"center"}}>
          <span style={{fontSize:"11px",color:locked?"#3a8060":"#4a6878"}}>
            {locked?"Passport locked.":selectedSources.size>0?`${selectedSources.size} sources`:"Select sources"}
          </span>
          {!locked&&selectedSources.size>0&&(
            <button className="ab pri" onClick={doGenerate}>Generate Gravity Map</button>
          )}
          <button className="ab gho" onClick={()=>{setMessages([{role:"assistant",content:WELCOME}]);setPassport({});setInput("");setLocked(false);setReady(false);setSelectedSources(new Set());}}>Reset</button>
        </div>
      </div>

      {/* Body */}
      <div style={{display:"flex",flex:1,overflow:"hidden",minHeight:0}}>
        {/* Left */}
        <div style={{width:"46%",borderRight:"1px solid #0c1620",display:"flex",flexDirection:"column",overflow:"hidden"}}>
          <div style={{display:"flex",borderBottom:"1px solid #111d2b",flexShrink:0}}>
            {["ai","manual"].map(m=>(
              <button key={m} onClick={()=>setMode(m)} style={{
                flex:1,padding:"5px 0",fontSize:11,letterSpacing:".06em",fontWeight:500,
                fontFamily:"var(--font-sans)",cursor:"pointer",border:"none",
                borderBottom:mode===m?"2px solid #c8922a":"2px solid transparent",
                background:"transparent",color:mode===m?"#c8922a":"#c0ccd4",transition:"all .15s"
              }}>{m==="ai"?"AI Declaration":"Manual Form"}</button>
            ))}
          </div>

          {mode==="ai"?(<>
            <div style={{flex:1,overflow:"auto",padding:"8px 10px"}}>
              {messages.map((m,i)=>(
                <div key={i} style={m.role==="user"
                  ?{background:"#0a0e18",borderLeft:"2px solid #c8922a",padding:"5px 10px",borderRadius:"0 4px 4px 0",margin:"3px 0",lineHeight:1.5,whiteSpace:"pre-wrap",color:"#a8bcc8"}
                  :{borderLeft:"2px solid #0e1a26",padding:"5px 10px",borderRadius:"0 4px 4px 0",margin:"3px 0",lineHeight:1.5,whiteSpace:"pre-wrap",color:"#506070"}
                }>{m.content}</div>
              ))}
              {loading&&<div style={{borderLeft:"2px solid #0e1a26",padding:"6px 10px",margin:"3px 0"}}><span className="dot"/><span className="dot"/><span className="dot"/></div>}
              <div ref={bottomRef}/>
            </div>
            <div style={{padding:"6px 10px",borderTop:"1px solid #0a1218",display:"flex",gap:"6px",flexShrink:0}}>
              <textarea className="tinp" rows={2} value={input} onChange={e=>setInput(e.target.value)} onKeyDown={onKey}
                placeholder={locked?"Passport locked.":"Declare your scene..."} disabled={loading||locked} style={{flex:1}}/>
              <button className="ab pri" onClick={sendAI} disabled={!input.trim()||loading||locked} style={{alignSelf:"flex-end"}}>Send</button>
            </div>
          </>):(
            <div style={{flex:1,overflow:"hidden",padding:"8px 10px",display:"flex",flexDirection:"column"}}>
              <div style={{marginBottom:8}}>
                <label style={fL}>Scene name</label>
                <input style={fI} defaultValue="my scene" onChange={e=>updateManual("scene_id",slugify(e.target.value)+"_v0_1")}/>
              </div>
              <div style={{marginBottom:8}}>
                <label style={fL}>Render mode</label>
                <div style={{display:"flex",gap:5}}>
                  {[{key:"static",label:"Static Frame",sub:"Frozen geometry"},{key:"animation",label:"Animation",sub:"N-body orbits"}].map(({key,label,sub})=>{
                    const active=renderMode===key;
                    return(
                      <button key={key} onClick={()=>setRenderMode(key)} style={{
                        flex:1,padding:"5px 3px",borderRadius:4,cursor:"pointer",
                        border:"1px solid "+(active?"#c8922a":"#1a2838"),
                        background:active?"#1a1200":"transparent",
                        transition:"all .15s",textAlign:"center"
                      }}>
                        <div style={{color:"#c8d8e8",fontSize:11,fontWeight:500}}>{label}</div>
                        <div style={{color:"#4a7080",fontSize:10}}>{sub}</div>
                      </button>
                    );
                  })}
                </div>
              </div>
              <div style={{marginBottom:8}}>
                <label style={fL}>Scene type</label>
                <div style={{display:"flex",gap:5}}>
                  {[{key:"SS",label:"Solar System",sub:"All planets + Sun"},{key:"LSN",label:"LSN",sub:"Local Stellar Neighborhood"},
                    {key:"ATOMS",label:"Atoms",sub:"Coming soon",disabled:true},{key:"MW",label:"Milky Way",sub:"Coming soon",disabled:true}
                  ].map(({key,label,sub,disabled})=>{
                    const active=(key==="SS"&&passport.purpose?.includes("solar"))||(key==="LSN"&&passport.purpose?.includes("stellar"));
                    return(
                      <button key={key} disabled={disabled} onClick={()=>applyPreset(key)} style={{
                        flex:1,padding:"5px 3px",borderRadius:4,cursor:disabled?"default":"pointer",
                        border:"1px solid "+(active?"#c8922a":disabled?"#0e1620":"#1a2838"),
                        background:active?"#1a1200":disabled?"#080a10":"transparent",
                        opacity:disabled?0.35:1,transition:"all .15s",textAlign:"center"
                      }}>
                        <div style={{color:disabled?"#2a4060":"#c8d8e8",fontSize:11,fontWeight:500}}>{label}</div>
                        <div style={{color:disabled?"#1e3040":"#4a7080",fontSize:10}}>{sub}</div>
                      </button>
                    );
                  })}
                </div>
              </div>
              <div style={{display:"flex",flexDirection:"column",flex:"1 1 0",minHeight:0}}>
                <label style={fL}>Sources ({selectedSources.size} selected)</label>
                <div style={{overflow:"auto",flex:1,border:"1px solid #111d2b",borderRadius:4}}>
                  {allSources.map(({group,items})=>(
                    <div key={group}>
                      <div style={{padding:"2px 8px",fontSize:10,color:"#4a7888",background:"#0a0d16",letterSpacing:".08em",textTransform:"uppercase",position:"sticky",top:0,zIndex:1}}>{group}</div>
                      {items.map(s=>(
                        <label key={s.id} style={{display:"flex",alignItems:"center",gap:6,padding:"3px 8px",cursor:"pointer",borderBottom:"1px solid #090d16",background:selectedSources.has(s.id)?"#0e1828":"transparent"}}>
                          <input type="checkbox" style={{accentColor:"#c8922a",flexShrink:0}} checked={selectedSources.has(s.id)} onChange={()=>toggleSource(s.id)}/>
                          <span style={{flex:1,color:"#b0c4d4"}}>{s.name}</span>
                          <span style={{color:"#4a7080",fontSize:10,fontFamily:"var(--font-mono)",textAlign:"right"}}>
                            {s.dist_pc!==undefined?`${s.dist_pc} pc`:s.dist_au?`${s.dist_au} AU`:""}
                          </span>
                        </label>
                      ))}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Right: passport JSON */}
        <div style={{flex:1,display:"flex",flexDirection:"column",overflow:"hidden"}}>
          <div style={{padding:"4px 10px",borderBottom:"1px solid #0a1218",display:"flex",justifyContent:"space-between",alignItems:"center",fontSize:"10px",letterSpacing:".1em",textTransform:"uppercase",color:"#c0ccd4",fontWeight:500,flexShrink:0}}>
            <span>Scene passport</span>
            <span style={{color:fc>0?"#7a5010":"#c0ccd4"}}>{fc} field{fc!==1?"s":""} declared</span>
          </div>
          <div style={{flex:1,overflow:"auto",padding:"8px 10px",fontFamily:"var(--font-mono)",fontSize:"11px",lineHeight:1.6}}
            dangerouslySetInnerHTML={{__html:hl(fc>0?JSON.stringify(passport,null,2):"{}") }}/>
        </div>
      </div>
    </div>
  );
}

// ── STAGE SCREEN ─────────────────────────────────────────────────────────────

function StageScreen({ passport, onBack }) {
  const containerRef = useRef(null);
  const rendRef      = useRef(null);
  const camRef       = useRef(null);
  const animRef      = useRef(null);
  const sceneRef     = useRef(null);
  const orbitRef     = useRef({theta:0.4,phi:1.1,radius:120,isDown:false,lastX:0,lastY:0,lastDist:0,lookAt:[0,0,0]});
  const maxDRef      = useRef(1);
  const camTarget    = useRef(null); // {targetRadius,targetPhi,targetTheta,lookAt,progress}

  // Three.js layer object refs
  const gcsNewtonRef  = useRef(null);
  const gcs1pnRef     = useRef(null);
  const eigenNewtonRef= useRef(null);
  const eigen1pnRef   = useRef(null);
  const networkRef    = useRef(null);
  const sourceMeshes  = useRef({});

  // Animation state lives outside React to avoid render-loop re-renders
  const animState = useRef({playing:false,speed:1,step:0,frame:0,dt:0.005,srcs:null});

  // React state
  const [panelOpen,  setPanelOpen]  = useState(false);
  const [computing,  setComputing]  = useState(false);
  const [computed,   setComputed]   = useState(false);
  const [physMode,   setPhysMode]   = useState('newton');  // 'newton' | '1pn'
  const [layersOn,   setLayersOn]   = useState({gcs:true, eigen:false, network:false});
  const [opacity,    setOpacity]    = useState({gcs:0.8,  eigen:0.7,  network:0.4});
  const [playing,    setPlaying]    = useState(false);
  const [speed,      setSpeed]      = useState(1);
  const [stepDisp,   setStepDisp]   = useState(0);

  const geoStore = useRef({gcsPts:[],gcsPts1pn:[],eigenPts:[],eigenPts1pn:[],srcs:[]});

  const isAnimated = passport.render_mode === 'animation';
  const activeSources = (passport.active_sources||[])
    .map(id=>ALL_SOURCES.find(s=>s.id===id)).filter(Boolean);

  // ── Three.js init (once) ──────────────────────────────────────────────────
  useEffect(()=>{
    const el=containerRef.current; if(!el)return;
    const W=el.clientWidth,H=el.clientHeight;

    const scene=new THREE.Scene();
    scene.background=new THREE.Color(0x07090d);
    scene.fog=new THREE.FogExp2(0x07090d,0.0003);
    sceneRef.current=scene;

    const cam=new THREE.PerspectiveCamera(55,W/H,0.0001,5000);
    camRef.current=cam;

    const ren=new THREE.WebGLRenderer({antialias:true});
    ren.setPixelRatio(Math.min(window.devicePixelRatio,2));
    ren.setSize(W,H);
    el.appendChild(ren.domElement);
    rendRef.current=ren;

    // Background stars
    const bgGeo=new THREE.BufferGeometry();
    const bgPos=new Float32Array(3000*3);
    for(let i=0;i<bgPos.length;i++) bgPos[i]=(Math.random()-0.5)*4000;
    bgGeo.setAttribute('position',new THREE.BufferAttribute(bgPos,3));
    scene.add(new THREE.Points(bgGeo,new THREE.PointsMaterial({color:0x8090a0,size:0.25,sizeAttenuation:true})));

    // Source spheres
    const n=activeSources.length;
    const positions=activeSources.map((s,i)=>sourcePos(s,i,n));
    const solIdx=activeSources.findIndex(s=>s.id==='SOL');
    if(solIdx>=0) positions[solIdx]=[0,0,0];
    // Moon relative to Earth
    const _ei=activeSources.findIndex(s=>s.id==='EARTH'), _mi=activeSources.findIndex(s=>s.id==='MOON');
    if(_ei>=0&&_mi>=0){const ma=ORBITAL_ANGLES['MOON']||0;positions[_mi]=[positions[_ei][0]+0.00257*Math.cos(ma),positions[_ei][1],positions[_ei][2]+0.00257*Math.sin(ma)];}

    // Detect AU-scale scene: majority of non-Sol sources use dist_au (not dist_pc)
    const nonSol=activeSources.filter(s=>s.id!=='SOL');
    const scaleAU=nonSol.length>0&&nonSol.filter(s=>s.dist_au!==undefined&&s.dist_pc===undefined).length>nonSol.length/2;

    activeSources.forEach((s,i)=>{
      const geo=new THREE.SphereGeometry(starSize(s,scaleAU),24,16);
      const col=starColorHex(s.cls);
      const emI=s.id==='SOL'?(scaleAU?0.8:2.0):0.5;
      const mat=new THREE.MeshStandardMaterial({color:col,emissive:col,emissiveIntensity:emI,roughness:0.5,metalness:0.0});
      const mesh=new THREE.Mesh(geo,mat);
      mesh.position.set(...positions[i]);
      scene.add(mesh);
      sourceMeshes.current[s.id]=mesh;
    });

    scene.add(new THREE.AmbientLight(0x1a2840,1.2));
    const sl=new THREE.PointLight(0xFFE080,3.0,800); sl.position.set(0,0,0); scene.add(sl);

    const maxD=Math.max(...positions.map(([x,y,z])=>Math.sqrt(x*x+y*y+z*z)),1);
    maxDRef.current=maxD;
    const o=orbitRef.current; o.radius=maxD*2.8; o.lookAt=[0,0,0];
    const updateCam=()=>{
      const la=o.lookAt;
      cam.position.set(la[0]+o.radius*Math.sin(o.phi)*Math.cos(o.theta),la[1]+o.radius*Math.cos(o.phi),la[2]+o.radius*Math.sin(o.phi)*Math.sin(o.theta));
      cam.lookAt(la[0],la[1],la[2]);
    };
    updateCam();

    // Orbit controls
    const md=e=>{o.isDown=true;o.lastX=e.clientX;o.lastY=e.clientY;};
    const mm=e=>{if(!o.isDown||camTarget.current)return;o.theta-=(e.clientX-o.lastX)*0.007;o.phi=Math.max(0.05,Math.min(Math.PI-0.05,o.phi-(e.clientY-o.lastY)*0.007));o.lastX=e.clientX;o.lastY=e.clientY;updateCam();};
    const mu=()=>{o.isDown=false;};
    const mw=e=>{o.radius=Math.max(0.001,Math.min(maxD*8,o.radius*(1+e.deltaY*0.001)));updateCam();};
    const ts=e=>{if(e.touches.length===1){o.isDown=true;o.lastX=e.touches[0].clientX;o.lastY=e.touches[0].clientY;}if(e.touches.length===2)o.lastDist=Math.hypot(e.touches[0].clientX-e.touches[1].clientX,e.touches[0].clientY-e.touches[1].clientY);};
    const tm=e=>{e.preventDefault();if(camTarget.current)return;if(e.touches.length===1&&o.isDown){o.theta-=(e.touches[0].clientX-o.lastX)*0.007;o.phi=Math.max(0.05,Math.min(Math.PI-0.05,o.phi-(e.touches[0].clientY-o.lastY)*0.007));o.lastX=e.touches[0].clientX;o.lastY=e.touches[0].clientY;updateCam();}if(e.touches.length===2){const d=Math.hypot(e.touches[0].clientX-e.touches[1].clientX,e.touches[0].clientY-e.touches[1].clientY);o.radius=Math.max(0.001,Math.min(maxD*8,o.radius*(o.lastDist/d)));o.lastDist=d;updateCam();}};
    const te=()=>{o.isDown=false;o.lastDist=0;};
    ren.domElement.addEventListener('mousedown',md);
    window.addEventListener('mousemove',mm);
    window.addEventListener('mouseup',mu);
    ren.domElement.addEventListener('wheel',mw,{passive:true});
    ren.domElement.addEventListener('touchstart',ts,{passive:true});
    ren.domElement.addEventListener('touchmove',tm,{passive:false});
    ren.domElement.addEventListener('touchend',te);
    const onResize=()=>{const w=el.clientWidth,h=el.clientHeight;ren.setSize(w,h);cam.aspect=w/h;cam.updateProjectionMatrix();};
    window.addEventListener('resize',onResize);

    // Main render loop
    const loop=()=>{
      animRef.current=requestAnimationFrame(loop);
      const as=animState.current;
      if(isAnimated&&as.playing&&as.srcs){
        const steps=Math.max(1,Math.round(as.speed));
        for(let i=0;i<steps;i++) as.srcs=leapfrogStep(as.srcs,as.dt);
        as.step+=steps; as.frame++;
        // Update source sphere positions
        for(const s of as.srcs){
          const m=sourceMeshes.current[s.id];
          if(m) m.position.set(...s.pos);
        }
        // Re-extract GCS every 8 frames during animation (scale for large scenes)
        const animInterval=as.srcs.length>20?16:8;
        if(as.frame%animInterval===0){
          const aN=as.srcs.length,aRays=fibRays(aN<=10?80:aN<=20?50:30),aRad=aN<=10?12:aN<=20?8:6;
          const allPts=[];
          for(const s of as.srcs) allPts.push(...extractGCS(as.srcs,s.id,aRays,aRad,false));
          const obj=gcsNewtonRef.current;
          if(obj){
            const attr=obj.geometry.attributes.position;
            for(let i=0;i<allPts.length&&i*3+2<attr.array.length;i++){
              attr.array[i*3]=allPts[i][0];attr.array[i*3+1]=allPts[i][1];attr.array[i*3+2]=allPts[i][2];
            }
            for(let i=allPts.length*3;i<attr.array.length;i++) attr.array[i]=0;
            attr.needsUpdate=true;
            obj.geometry.setDrawRange(0,allPts.length);
          }
          setStepDisp(as.step);
        }
      }
      // Smooth camera fly-to animation
      const ct=camTarget.current;
      if(ct){
        ct.progress=Math.min(1,ct.progress+0.025);
        const t=ct.progress,ease=t<0.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
        o.radius=ct._r0+(ct.targetRadius-ct._r0)*ease;
        o.theta=ct._t0+(ct.targetTheta-ct._t0)*ease;
        o.phi=ct._p0+(ct.targetPhi-ct._p0)*ease;
        o.lookAt=[
          ct._la0[0]+(ct.lookAt[0]-ct._la0[0])*ease,
          ct._la0[1]+(ct.lookAt[1]-ct._la0[1])*ease,
          ct._la0[2]+(ct.lookAt[2]-ct._la0[2])*ease,
        ];
        updateCam();
        if(ct.progress>=1) camTarget.current=null;
      }
      ren.render(scene,cam);
    };
    loop();

    return()=>{
      cancelAnimationFrame(animRef.current);
      window.removeEventListener('mousemove',mm);window.removeEventListener('mouseup',mu);window.removeEventListener('resize',onResize);
      ren.dispose(); if(el.contains(ren.domElement))el.removeChild(ren.domElement);
    };
  },[]);

  // ── Zoom-to-source ──────────────────────────────────────────────────────
  const zoomToSource=sourceId=>{
    const mesh=sourceMeshes.current[sourceId];
    if(!mesh)return;
    const pos=[mesh.position.x,mesh.position.y,mesh.position.z];
    const srcs=geoStore.current.srcs||[];
    // View distance: use GCS shell radius but cap so we're always zooming IN
    const csrc=srcs.find(s=>s.id===sourceId);
    let viewDist=0.5;
    if(csrc&&srcs.length>1){
      const rm=gcsRmax(srcs,sourceId);
      // Use 1.5× shell radius, but never more than 30% of the source's distance from origin
      const orbitalDist=Math.sqrt(pos[0]**2+pos[1]**2+pos[2]**2);
      viewDist=Math.min(rm*1.5, Math.max(orbitalDist*0.3, 0.05));
    }
    viewDist=Math.max(viewDist,0.005);
    const o=orbitRef.current;
    camTarget.current={
      targetRadius:viewDist,targetTheta:0.4,targetPhi:1.1,
      lookAt:pos,progress:0,
      _r0:o.radius,_t0:o.theta,_p0:o.phi,_la0:[...o.lookAt],
    };
  };
  const zoomToFullScene=()=>{
    const o=orbitRef.current;
    camTarget.current={
      targetRadius:maxDRef.current*2.8,targetTheta:0.4,targetPhi:1.1,
      lookAt:[0,0,0],progress:0,
      _r0:o.radius,_t0:o.theta,_p0:o.phi,_la0:[...o.lookAt],
    };
  };

  // Panel resize
  useEffect(()=>{
    if(!rendRef.current||!camRef.current||!containerRef.current)return;
    setTimeout(()=>{const w=containerRef.current.clientWidth,h=containerRef.current.clientHeight;rendRef.current.setSize(w,h);camRef.current.aspect=w/h;camRef.current.updateProjectionMatrix();},320);
  },[panelOpen]);

  // ── Compute geometry from passport ───────────────────────────────────────
  useEffect(()=>{
    if(!activeSources.length)return;
    setComputing(true); setComputed(false);
    setTimeout(()=>{
      const srcs=passportToComputeSources(activeSources);
      const N=srcs.length;
      // Adaptive sampling: scale down rays/radial for large source counts
      const nRays=N<=10?200:N<=20?120:N<=35?80:50;
      const nRad=N<=10?30:N<=20?20:N<=35?14:10;
      const nEig=N<=10?30:N<=20?20:12;
      const rays=fibRays(nRays);

      const gcsPts=[],gcsPts1pn=[],eigenPts=[],eigenPts1pn=[];
      for(const s of srcs){
        const before=gcsPts.length;
        gcsPts.push(...extractGCS(srcs,s.id,rays,nRad,false));
        gcsPts1pn.push(...extractGCS(srcs,s.id,rays,nRad,true));
        const r=gcsRmax(srcs,s.id)*0.55;
        eigenPts.push(...extractEigenframe(srcs,s.id,nEig,r,false));
        eigenPts1pn.push(...extractEigenframe(srcs,s.id,nEig,r,true));
        console.log('[Atlas] GCS',s.id,':',(gcsPts.length-before),'pts   rmax=',gcsRmax(srcs,s.id).toFixed(4));
      }
      console.log('[Atlas] Total GCS:',gcsPts.length,'Newton |',gcsPts1pn.length,'1PN | eigenPts:',eigenPts.length);
      geoStore.current={gcsPts,gcsPts1pn,eigenPts,eigenPts1pn,srcs};
      animState.current.srcs=circularOrbits(srcs);

      rebuildLayers(gcsPts,gcsPts1pn,eigenPts,eigenPts1pn,srcs);
      setComputing(false); setComputed(true);
    },50);
  },[passport.active_sources?.join(',')]);

  // ── Build / rebuild Three.js layer objects ────────────────────────────────
  const disposeObj=ref=>{
    if(!ref.current)return;
    sceneRef.current?.remove(ref.current);
    ref.current.geometry?.dispose();
    ref.current.material?.dispose();
    ref.current=null;
  };

  const makePointCloud=(pts,color,opacity,visible)=>{
    const MAX=Math.max(pts.length*2,500);
    const buf=new Float32Array(MAX*3).fill(0);
    pts.forEach((p,i)=>{buf[i*3]=p[0];buf[i*3+1]=p[1];buf[i*3+2]=p[2];});
    const geo=new THREE.BufferGeometry();
    const attr=new THREE.BufferAttribute(buf,3); attr.setUsage(THREE.DynamicDrawUsage);
    geo.setAttribute('position',attr);
    geo.setDrawRange(0,pts.length);
    // depthTest:false ensures GCS diagnostic overlay always renders on top of source spheres.
    const mat=new THREE.PointsMaterial({color,size:3.0,sizeAttenuation:false,transparent:true,opacity,depthWrite:false,depthTest:false});
    const obj=new THREE.Points(geo,mat); obj.visible=visible;
    obj.renderOrder=999;
    // frustumCulled:false prevents THREE.js from culling the entire cloud.
    // computeBoundingSphere() uses the FULL buffer (including unused padding),
    // which would place the bounding sphere far beyond the camera far plane.
    obj.frustumCulled=false;
    return obj;
  };

  const makeEigenLines=(pts,opacity,visible)=>{
    const LEN=0.025; const posArr=[],colArr=[];
    for(const{pos,dir,val}of pts){
      const h=vscale(dir,LEN*0.5);
      posArr.push(pos[0]-h[0],pos[1]-h[1],pos[2]-h[2],pos[0]+h[0],pos[1]+h[1],pos[2]+h[2]);
      // Blue = compression (neg eigenvalue), gold = extension (pos)
      const t=Math.max(0,Math.min(1,(val+0.3)/0.6));
      const r=t*0.8,g=t*0.5,b=1-t*0.8;
      colArr.push(r,g,b,r,g,b);
    }
    if(!posArr.length)return null;
    const geo=new THREE.BufferGeometry();
    geo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(posArr),3));
    geo.setAttribute('color',new THREE.BufferAttribute(new Float32Array(colArr),3));
    const mat=new THREE.LineBasicMaterial({vertexColors:true,transparent:true,opacity});
    const obj=new THREE.LineSegments(geo,mat); obj.visible=visible;
    return obj;
  };

  const rebuildLayers=(gcsPts,gcsPts1pn,eigenPts,eigenPts1pn,srcs)=>{
    const scene=sceneRef.current; if(!scene)return;
    [gcsNewtonRef,gcs1pnRef,eigenNewtonRef,eigen1pnRef,networkRef].forEach(disposeObj);

    // GCS Newton (orange-amber)
    const gn=makePointCloud(gcsPts,0xd4a017,opacity.gcs,layersOn.gcs&&physMode==='newton');
    scene.add(gn); gcsNewtonRef.current=gn;

    // GCS 1PN (cyan)
    const gp=makePointCloud(gcsPts1pn,0xc8922a,opacity.gcs,layersOn.gcs&&physMode==='1pn');
    scene.add(gp); gcs1pnRef.current=gp;

    // Eigenframe Newton
    const en=makeEigenLines(eigenPts,opacity.eigen,layersOn.eigen&&physMode==='newton');
    if(en){scene.add(en);eigenNewtonRef.current=en;}

    // Eigenframe 1PN
    const ep=makeEigenLines(eigenPts1pn,opacity.eigen,layersOn.eigen&&physMode==='1pn');
    if(ep){scene.add(ep);eigen1pnRef.current=ep;}

    // Source network (dim lines to 2 nearest neighbours)
    const netPos=[];
    for(const si of srcs){
      const near=srcs.filter(sj=>sj.id!==si.id)
        .map(sj=>({sj,d:vnorm(vsub(si.pos,sj.pos))}))
        .sort((a,b)=>a.d-b.d).slice(0,2);
      for(const{sj}of near) netPos.push(...si.pos,...sj.pos);
    }
    if(netPos.length){
      const geo=new THREE.BufferGeometry();
      geo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(netPos),3));
      const net=new THREE.LineSegments(geo,new THREE.LineBasicMaterial({color:0x203040,transparent:true,opacity:opacity.network}));
      net.visible=layersOn.network;
      scene.add(net); networkRef.current=net;
    }
  };

  // ── Layer visibility sync ─────────────────────────────────────────────────
  useEffect(()=>{
    if(!computed)return;
    const pm=physMode;
    const setVis=(ref,vis,op)=>{if(!ref.current)return;ref.current.visible=vis;if(ref.current.material)ref.current.material.opacity=op;};
    setVis(gcsNewtonRef,  layersOn.gcs  && pm==='newton', opacity.gcs);
    setVis(gcs1pnRef,     layersOn.gcs  && pm==='1pn',    opacity.gcs);
    setVis(eigenNewtonRef,layersOn.eigen && pm==='newton', opacity.eigen);
    setVis(eigen1pnRef,   layersOn.eigen && pm==='1pn',    opacity.eigen);
    setVis(networkRef,    layersOn.network,                opacity.network);
  },[layersOn,opacity,physMode,computed]);

  // ── Animation controls ───────────────────────────────────────────────────
  const togglePlay=()=>{
    const next=!animState.current.playing;
    animState.current.playing=next;
    setPlaying(next);
  };
  const resetAnim=()=>{
    animState.current.playing=false; animState.current.step=0; animState.current.frame=0;
    animState.current.srcs=circularOrbits(geoStore.current.srcs);
    setPlaying(false); setStepDisp(0);
    for(const s of animState.current.srcs){
      const m=sourceMeshes.current[s.id]; if(m)m.position.set(...s.pos);
    }
    // Restore static GCS
    const obj=gcsNewtonRef.current;
    if(obj&&geoStore.current.gcsPts.length){
      const attr=obj.geometry.attributes.position;
      geoStore.current.gcsPts.forEach((p,i)=>{attr.array[i*3]=p[0];attr.array[i*3+1]=p[1];attr.array[i*3+2]=p[2];});
      attr.needsUpdate=true;
      obj.geometry.setDrawRange(0,geoStore.current.gcsPts.length);
    }
  };
  const handleSpeed=v=>{animState.current.speed=parseFloat(v);setSpeed(parseFloat(v));};

  // ── Colors / labels ───────────────────────────────────────────────────────
  const modeColor={newton:'#d4a017','1pn':'#c8922a'};
  const modeLabel={newton:'NEWTONIAN  R2','1pn':'1PN CORRECTED  R5'};
  const modeDesc={
    newton:'Linearized tidal operator. Sources superposed independently. Standard Newtonian gravity boundaries.',
    '1pn':  '1PN-corrected operator. Cross-terms break superposition. Self-coupling weakens context field. Jurisdiction expands.',
  };

  // ── Render ────────────────────────────────────────────────────────────────
  return (
    <div style={{position:'relative',width:'100%',height:'100%',background:'#07090d',overflow:'hidden',display:'flex'}}>
      <style>{`
        input[type=range]{accent-color:#c8922a;width:100%;margin:3px 0;}
        .tog{width:34px;height:19px;border-radius:10px;cursor:pointer;position:relative;transition:background .2s;flex-shrink:0;border:none;}
        .tog-knob{position:absolute;top:2px;width:15px;height:15px;border-radius:50%;background:#c0ccd4;transition:left .2s;}
        .mode-pill{font-family:var(--font-sans);font-size:10px;font-weight:600;letter-spacing:.09em;padding:6px 10px;border-radius:5px;cursor:pointer;border:1px solid;transition:all .2s;flex:1;text-align:center;}
        .ctrl{font-family:var(--font-sans);font-size:12px;font-weight:500;padding:5px 12px;border-radius:4px;cursor:pointer;background:transparent;border:1px solid #1a2838;color:#c0ccd4;transition:all .15s;}
        .ctrl:hover{border-color:#c8922a;color:#c8922a;}
        .ctrl.on{background:#1a1200;border-color:#c8922a;color:#c8922a;}
        @keyframes pulse{0%,100%{opacity:.6}50%{opacity:1}}
        .computing{animation:pulse 1.2s ease-in-out infinite;}
      `}</style>

      {/* Canvas container */}
      <div ref={containerRef} style={{flex:1,height:'100%',transition:'flex .3s ease',overflow:'hidden',position:'relative'}}>
        {computing&&(
          <div className="computing" style={{position:'absolute',top:'50%',left:'50%',transform:'translate(-50%,-50%)',zIndex:50,textAlign:'center',pointerEvents:'none'}}>
            <div style={{color:'#c8922a',fontSize:13,letterSpacing:'.1em',fontFamily:'var(--font-sans)'}}>COMPUTING GEOMETRY</div>
            <div style={{color:'#4a6878',fontSize:11,marginTop:5,fontFamily:'var(--font-sans)'}}>R2 + R5 extraction · eigenframe sampling</div>
          </div>
        )}

        {/* Animation bar (only in animation mode) */}
        {computed&&isAnimated&&(
          <div style={{position:'absolute',bottom:16,left:'50%',transform:'translateX(-50%)',zIndex:20,display:'flex',alignItems:'center',gap:10,background:'rgba(7,9,13,0.92)',border:'1px solid #1a2838',borderRadius:8,padding:'7px 16px',backdropFilter:'blur(8px)',fontFamily:'var(--font-sans)'}}>
            <button className={`ctrl${playing?' on':''}`} onClick={togglePlay} style={{minWidth:64}}>
              {playing?'⏸ Pause':'▶ Play'}
            </button>
            <button className="ctrl" onClick={resetAnim} title="Reset">↺</button>
            <div style={{display:'flex',alignItems:'center',gap:6,color:'#4a6878',fontSize:11}}>
              <span>Speed</span>
              <input type="range" min={0.5} max={6} step={0.5} value={speed} onChange={e=>handleSpeed(e.target.value)} style={{width:64}}/>
              <span style={{color:'#c8922a',minWidth:18,fontSize:12}}>{speed}×</span>
            </div>
            <div style={{color:'#2a4a60',fontSize:11,minWidth:56}}>step {stepDisp}</div>
          </div>
        )}
      </div>

      {/* Side panel */}
      <div style={{width:panelOpen?'268px':'0',minWidth:panelOpen?'268px':'0',height:'100%',background:'rgba(7,9,13,0.97)',borderLeft:panelOpen?'1px solid #111d2b':'none',overflow:'hidden',transition:'width .3s ease,min-width .3s ease',display:'flex',flexDirection:'column',flexShrink:0}}>
        <div style={{padding:'56px 14px 20px',overflowY:'auto',flex:1,fontFamily:'var(--font-sans)'}}>

          {/* Scene */}
          <div style={{marginBottom:16,paddingBottom:12,borderBottom:'1px solid #111d2b'}}>
            <div style={{color:'#c8922a',fontSize:10,fontWeight:500,letterSpacing:'.12em',textTransform:'uppercase',marginBottom:5}}>Scene</div>
            <div style={{color:'#c0ccd4',fontSize:13}}>{passport.scene_id||'unnamed'}</div>
            <div style={{color:'#5a8090',fontSize:12,marginTop:3}}>
              {activeSources.length} sources · {computed?<span style={{color:'#2a6040'}}>geometry ready</span>:computing?<span style={{color:'#7a5010'}}>computing…</span>:'—'}
            </div>
          </div>

          {/* Physics mode */}
          <div style={{marginBottom:16,paddingBottom:14,borderBottom:'1px solid #111d2b'}}>
            <div style={{color:'#c8922a',fontSize:10,fontWeight:500,letterSpacing:'.12em',textTransform:'uppercase',marginBottom:8}}>Physics Mode</div>
            <div style={{display:'flex',gap:6,marginBottom:8}}>
              {['newton','1pn'].map(key=>(
                <button key={key} className="mode-pill" onClick={()=>setPhysMode(key)} style={{
                  background:physMode===key?`rgba(${key==='1pn'?'16,184,204':'204,102,16'},0.12)`:'transparent',
                  borderColor:physMode===key?modeColor[key]:'#1a2838',
                  color:physMode===key?modeColor[key]:'#4a6878',
                }}>
                  {modeLabel[key]}
                </button>
              ))}
            </div>
            <div style={{fontSize:11,color:'#2a4060',lineHeight:1.6}}>{modeDesc[physMode]}</div>
            {computed&&(
              <div style={{marginTop:8,fontSize:10,color:'#2a4050',lineHeight:1.5}}>
                Newton: <span style={{color:'#8a4208'}}>●</span> {geoStore.current.gcsPts.length.toLocaleString()} pts
                &nbsp;·&nbsp;
                1PN: <span style={{color:'#087888'}}>●</span> {geoStore.current.gcsPts1pn.length.toLocaleString()} pts
              </div>
            )}
          </div>

          {/* Layers */}
          <div style={{color:'#c8922a',fontSize:10,fontWeight:500,letterSpacing:'.12em',textTransform:'uppercase',marginBottom:10}}>Layers</div>
          {[
            {key:'gcs',    label:'Diagnostic Parity Geometry', desc:physMode==='newton'?'R2 linearized GCS shells':'R5 1PN-corrected GCS shells', color:modeColor[physMode]},
            {key:'eigen',  label:'Tidal Eigenframe',   desc:'Principal compression axis — eigenvector of E_ij', color:'#4466bb'},
            {key:'network',label:'Source Network',     desc:'Nearest-neighbour relational links',              color:'#304050'},
          ].map(({key,label,desc,color})=>(
            <div key={key} style={{marginBottom:14}}>
              <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,marginBottom:3}}>
                <div>
                  <div style={{color:layersOn[key]?'#c8d8e8':'#4a6878',fontSize:12,fontWeight:500,lineHeight:1.3}}>{label}</div>
                  <div style={{fontSize:10,color:computed&&layersOn[key]?'#2a5040':'#1a2e3a',marginTop:2,lineHeight:1.4}}>{desc}</div>
                </div>
                <button className="tog" style={{background:layersOn[key]?color:'#1a2838'}}
                  onClick={()=>setLayersOn(l=>({...l,[key]:!l[key]}))}>
                  <div className="tog-knob" style={{left:layersOn[key]?17:2}}/>
                </button>
              </div>
              {layersOn[key]&&(
                <input type="range" min={5} max={100} value={Math.round(opacity[key]*100)}
                  onChange={e=>setOpacity(o=>({...o,[key]:e.target.value/100}))}/>
              )}
            </div>
          ))}

          {/* Navigate — zoom to source */}
          {computed&&(
            <div style={{marginTop:4,marginBottom:16,paddingBottom:14,borderBottom:'1px solid #111d2b'}}>
              <div style={{color:'#c8922a',fontSize:10,fontWeight:500,letterSpacing:'.12em',textTransform:'uppercase',marginBottom:8}}>Navigate</div>
              <button className="ctrl" onClick={zoomToFullScene} style={{width:'100%',marginBottom:6,fontSize:11}}>Full Scene</button>
              <div style={{display:'flex',flexWrap:'wrap',gap:4}}>
                {activeSources.map(s=>(
                  <button key={s.id} className="ctrl" onClick={()=>zoomToSource(s.id)} style={{fontSize:10,padding:'3px 8px'}}>
                    <span style={{color:starColor(s.cls),marginRight:3}}>●</span>{s.name}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Claim note */}
          <div style={{marginTop:12,paddingTop:10,borderTop:'1px solid #0e1820',fontSize:10,color:'#1a2e3a',lineHeight:1.6}}>
            Atlas GCS geometry is a diagnostic computed over declared classical point sources. Not physical membranes, force boundaries, or observational claims. C_vis={C_VIS} (toy parameter for pedagogical visibility of 1PN correction).<br/>
            claim_status: diagnostic_candidate_not_observational
          </div>

          <button onClick={onBack} style={{marginTop:14,width:'100%',padding:'9px 0',background:'transparent',border:'1px solid #1a2838',color:'#c0ccd4',fontSize:13,fontFamily:'var(--font-sans)',borderRadius:5,cursor:'pointer'}}>
            ← Passport
          </button>
        </div>
      </div>

      {/* Controls toggle */}
      <button onClick={()=>setPanelOpen(p=>!p)} style={{position:'absolute',top:14,right:14,zIndex:200,background:'rgba(8,10,14,0.88)',border:'1px solid #1a2838',color:'#c0ccd4',fontFamily:'var(--font-sans)',fontSize:13,fontWeight:500,padding:'8px 16px',borderRadius:5,cursor:'pointer',backdropFilter:'blur(8px)',transition:'all .15s'}}>
        {panelOpen?'Hide':'Controls'}
      </button>
    </div>
  );
}

// ── ROOT ──────────────────────────────────────────────────────────────────────

export default function AtlasInstrument() {
  const [phase,   setPhase]   = useState("passport");
  const [passport,setPassport]= useState({});
  const [opacity, setOpacity] = useState(1);

  const fadeTo=fn=>{setOpacity(0);setTimeout(()=>{fn();setOpacity(1);},380);};

  return (
    <div style={{width:'100%',height:'100%',overflow:'hidden',opacity,transition:'opacity 0.38s ease'}}>
      {phase==='passport'
        ?<PassportScreen onGenerate={p=>fadeTo(()=>{setPassport(p);setPhase('stage');})}/>
        :<StageScreen passport={passport} onBack={()=>fadeTo(()=>setPhase('passport'))}/>}
    </div>
  );
}

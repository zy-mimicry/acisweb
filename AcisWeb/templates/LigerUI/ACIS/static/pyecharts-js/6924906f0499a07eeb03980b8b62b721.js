(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('郧西县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"420322","properties":{"name":"郧西县","cp":[110.425983,32.993182],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@A@KAIMGIIBITOJCDABIDIBIBC@EBCBA@GBCBGDOBI@EAA@@@CAA@@@C@GAA@C@A@C@IBC@IB@@E@KBA@C@@@A@@BA@@@@@GBGAGAAAG@G@GAC@A@GAIAEBEBABCBADCNADABCFGHA@GFGDID@BGBOJOFMDA@IBA@EBC@C@IDKFGFCBEDADADABAFADADG@E@GCC@E@IBKDGDCDA@EJABABCDC@G@GAIAE@@@G@ODA@IBIAC@C@CAG@GBC@CAC@CBCBCHA@ADABADEFEDABA@GBCBO@I@EAGAC@E@EDKJEDABABE@EBEAC@CCAEISAECA@A@@E@G@G@EAEAG@ICEAECECGGCAECC@C@C@GBKHGJAB@BABABCDCFCFCDCFGFGDABF^JRBF@F@\\BF@@BJJX@B@BHTBD@BBB@@@BDXBN@B@Z@HB@B\\FVBBBP@@@LAFCDABI@eJIH@@A@ABMDEDI@IDABIFOFCBIFIFA@EBGBGBEHGHEHEBCBCBMAG@SAA@SFU@O@I@MCMGKEIAA@E@E@IFCNEDKCIECGEAKHEFELIFMBODKDGDEBEDOFODM@I@KBKA]@I@E@SFOFGFIB@@EDLLLJFFVPPPJTDJBBDHLHVFNTDZFHHHXHXDXAHAHALCJCXIPC\\FFBFDAZ@RBD@B@B@FDFJFFHFBFBX@D@NIJEDM@SFEB@L@RJPFVALALQFGFC\\KTCJAFBLBRBZDTANAN@XBL@RD^JZHJBNBHAHAHAVKXEVC\\ELANELCBAHGFAZKTIBAPELARDPFFDLDNAJEB@@@HGDIZOTAPDHBXJLBPDLBD@NBVBXANARANFB@JD\\D@@@@@@@@@@NBB@DAPKJI@A@ALK@@@AA@@@@@A@@@@@@@@A@@B@@AA@@A@A@@BA@@B@@@@AB@@@@@@@@@@B@@B@@B@@B@@B@@@@B@@@@@B@@@@A@@B@@A@@@@@@B@@@@BB@@@B@@@@@BAHCLEJMJIHGJERCPBN@HBJDRHLBDBLBPDN@B@BAD@B@B@B@BAB@D@D@DA@@B@BABAB@D@BA\\ELEHBBB@@@@AB@@@@@B@@@@A@@@@@A@@@@@A@@@@@@@@@@@@@BBB@@BB@@@BB@@@@B@@@B@@@@@@@B@@B@@@@@@A@@@@@@@@B@@A@A@@@A@@@@@@@@@@@@@A@@@@B@@@@@@@@@@@@@BB@@@@@@@@@@@B@@A@@@@@@@@@@@@B@@@@@@@@@@@@B@@@@A@@@@@@@@@@BB@@@@A@@B@@@@@@@@@B@@@@@@B@@@@A@@@@@@@@@B@@B@@@@@@D@D@B@D@BABBB@@@D@BBB@BBBBBB@BBB@BBBBB@@BBB@D@B@BBB@B@BA@@@@BD@@@B@@@@@B@@@@@@@@@@B@@B@@@@@@@@@@BA@@@@@@BA@A@@@@@@@@@@@A@@@@@@@@@@@@@A@@BB@@@@BB@@BB@@@@@@@@B@@A@@@@@@@@@A@@@@@@@@@@@AA@@@@@A@@@@@A@@A@@@@@@@@@@B@@A@@@@@@@@@A@@@@@@@@A@@@AB@@A@@@A@@@@@@@@A@@@@@AB@@@BA@@@@@@@@@@@@BA@@@@@@@@A@@@@@@@@@D@B@B@BBBBB@RA@@B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@A@@@@A@@A@@@@@@@@B@@@@@@@@@@@@@@@@BB@@@@A@@@@@@@@@@@@@@@@BA@@@B@@@@@@@@@@@@B@@B@@@A@@@@B@@@@@@@@A@@@@@@@B@@B@BB@@@@@@@B@@@@@@@@@@@@@A@@B@@@@@@A@@@@@A@@@@@@B@@@@@@@@B@@@@@@@@@@@@@@@@@B@@@@@@@B@@@@@@@@@@@@B@@@@A@@@@@@B@@@@@@@@@H@TGRCJ@FDBB@@D@BBBBB@FBFB@@FBJBB@B@NEDCF@DAB@@AB@B@B@@AB@B@BB@@@B@@@@@@@@@@@@A@@@@@AB@@@@@@@@@@@@@@@@@@@@@@@@B@@@@@B@@@@@@@@B@@@@@@@@AB@B@@@@BB@@@B@@@@@@@@@@@@@@A@@@@@@@@@@@@B@@@@@@@@@@C@@@@@A@@@@@@B@@@@@@@@B@@@B@@B@@@@B@@@@@@B@@@@@B@@@@@@@BA@@@@@B@@@@@@@B@@B@@@@@@@@@@@@@@B@@@@@@BB@@@@@@@BB@@@@@@B@@A@@B@@@@@@@@@@B@@@@@@@B@B@@BB@@@@@@@@@@B@@@B@@@BB@@@@@A@@@@@@@@@@@A@@B@@B@@@@@@@@@@@B@@@@@@@BB@@@@@@@@@@B@@@B@@@@@B@@@@@B@@AB@@@@@@@B@@@@@@@@@@@@@@B@B@BA@@@@@@@@@@@@@A@@@@@@@@@@B@@@B@@@@B@@@@@@@@@@@@A@@@@B@@@@@@@@@B@@@@@@@@@@@@B@@A@@B@@@@@@@B@@@@@@@@@@@@BA@@B@@@@B@@@@@@@@@@@@@@@@A@@@@@@B@@@@@@@@@@@@@@@@BB@@B@@@@@@@@@@@@B@@@@@@@@@@@B@@@@@@@@@@@@B@@@@@@@@@@BB@BBBBB@@BBBBBDB@@DDB@BDBBBDDBBBBBBNDNHJFDVALJL@@NFL@dAPA@@LEHMFW@MDGHMHM@MBO@@BQ@A@OCMBKDEHINIRGNCRDJHPJLFNGJQFOHMDEHGCEEIKMGMOOEG@AAAA@@AAAGIEEMGSEGEIKEC@@IEEI@A@@@A@@@A@MAE@A@A@E@A@A@C@A@A@CAA@AA@C@ABABABC@A@@AA@@ABCBCBCBA@@BAD@BABC@ABAB@BAB@DA@@B@B@FAD@DADCBABADAB@BADCBAFECAC@EA@AAC@C@CE@C@EA@EBAHABBF@@EFABBH@BABAFCDAHEDAFC@A@AAA@@AA@@MAGAECCEAG@G@ABEDCFCBABA@C@GAECCEBEBEADC@ADE@CACAC@A@ABCDCBEAEACACDADGDGCACCGCAB@HBBEBE@ICA@GBI@C@ED@BCBCB@BEBA@@@AAAC@CCCAA@AHGBEFC@@DCDC@CCEACAC@CBAFCDCBGAAEACBE@@ECCCAE@CB@FBFDFBDCDC@CBCAMKGCE@@D@FBD@LC@AGAECAC@GAA@EA@CBC@EBA@CBG@E@CAECI@CBCDAFCBC@EAAAAAAICGAMEICAAEAAAAAIGKCIAK@ABI@EBABEBABADGHCDCH@BAD@B@D@B@DBF@B@DBDAD@D@D@BADA@I@GAIPGPADC@C@C@@AAA@EAEACACACGIKAEDABABCB@B@B@DAB@DCFAHAB@@A@A@AA@A@@@A@A@C@A@A@A@@@A@A@A@A@A@C@AACBAAA@C@C@C@A@AACCCCEAAE@E@C@ACBEACAAA@C@CAA@CAC@CBC@A@ABCB@B@BBBBBBBBBBB@BBB@BBB@BBB@BBBBD@BBBDFBN@FABAFA@AB@BC@CDGBGAEG@AAIAEIBQBKQCEACCAQKCAQEE@EASC@AKEA@GCA@A@@G@A@@AA@EEWSGSDC@"],"encodeOffsets":[[112938,33582]]}}],"UTF8Encoding":true});}));
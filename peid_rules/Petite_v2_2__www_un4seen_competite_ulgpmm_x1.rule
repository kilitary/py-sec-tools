rule _Petite_v2_2__www_un4seen_competite_ulgpmm
{
	meta:
		description = "Petite v2_2 __ www_un4seen_competite"
	strings:
		$a = {B800????00??00????????????????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

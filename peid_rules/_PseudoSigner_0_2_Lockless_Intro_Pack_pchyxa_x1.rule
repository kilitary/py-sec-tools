rule __PseudoSigner_0_2_Lockless_Intro_Pack_pchyxa
{
	meta:
		description = "_ PseudoSigner 0_2 _Lockless Intro Pack"
	strings:
		$a = {2CE8EB1A90905D8BC581EDF67390902B859090909083E8068985FF01ECAD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

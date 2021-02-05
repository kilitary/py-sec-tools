rule _WWPACK_v3_02_v3_02a_v3_04_Relocations_pack__bmbrer
{
	meta:
		description = "WWPACK v3_02_ v3_02a_ v3_04 _Relocations pack_"
	strings:
		$a = {BE????BF????B9????8CCD81ED????8BDD81EB????8BD3FCFA1E8EDB011533C02EAC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

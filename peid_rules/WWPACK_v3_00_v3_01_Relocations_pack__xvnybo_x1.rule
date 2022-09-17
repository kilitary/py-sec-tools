rule _WWPACK_v3_00_v3_01_Relocations_pack__xvnybo
{
	meta:
		description = "WWPACK v3_00_ v3_01 _Relocations pack_"
	strings:
		$a = {BE????BA????BF????B9????8CCD8EDD81ED????06068BDD2BDA8BD3FC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

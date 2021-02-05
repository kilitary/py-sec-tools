rule _WWPACK_v3_05c4_Extr_Passw_check_Vir_shield__sprfyb
{
	meta:
		description = "WWPACK v3_05c4 _Extr_ Passw_check_ Vir_ shield_"
	strings:
		$a = {0305C01AB8????8CCA03D08CC981C1????51B9????510606B1??518CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

rule _WWPACK_v3_05c4_Unextractable__Password_checking__wlwyfn
{
	meta:
		description = "WWPACK v3_05c4 _Unextractable _ Password checking_"
	strings:
		$a = {0305801BB8????8CCA03D08CC981C1????51B9????510606B1??518CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

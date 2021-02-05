rule _WWPACK_v3_05c4_Unextractable__Virus_Shield__edxdvf
{
	meta:
		description = "WWPACK v3_05c4 _Unextractable _ Virus Shield_"
	strings:
		$a = {0305401BB8????8CCA03D08CC981C1????51B9????510606B1??518CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

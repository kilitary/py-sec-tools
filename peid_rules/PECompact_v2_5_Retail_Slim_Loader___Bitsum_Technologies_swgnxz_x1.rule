rule _PECompact_v2_5_Retail_Slim_Loader___Bitsum_Technologies_swgnxz
{
	meta:
		description = "PECompact v2_5 Retail _Slim Loader_ __ Bitsum Technologies"
	strings:
		$a = {B8??????015064FF35000000006489250000000033C089085045433200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

rule _PeCompact_2_xx_Slim_Loader___BitSum_Technologies_upgsha
{
	meta:
		description = "PeCompact 2_xx _Slim Loader_ ___ BitSum Technologies"
	strings:
		$a = {B8????????5064FF35000000006489250000000033C089085045433200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

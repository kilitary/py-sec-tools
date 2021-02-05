rule _fasm__Tomasz_Grysztar_flat_lbswug
{
	meta:
		description = "fasm __ Tomasz Grysztar _flat"
	strings:
		$a = {535152565755E8000000005D8BCD81ED333040??2B8DEE32400083E90B898DF23240??80BDD13240??010F84}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

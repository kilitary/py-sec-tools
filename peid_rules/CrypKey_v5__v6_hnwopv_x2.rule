rule _CrypKey_v5__v6_hnwopv
{
	meta:
		description = "CrypKey v5 _ v6"
	strings:
		$a = {E8????????5883D80589C381C3????????8B436450}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

rule _Windows_Animation_format_ncisdd
{
	meta:
		description = "Windows Animation format"
	strings:
		$a = {558BEC83C4EC53????????8945ECB864400010E828EAFFFF33C05568CE51001064????????206A0068800000006A036A006A0168000000808D55EC33C0E8F6DBFFFF8B45ECE812E7FFFF50E83CEAFFFF8BD883FBFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

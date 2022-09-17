rule _ASProtect_vx_x_wdhhxo
{
	meta:
		description = "ASProtect vx_x"
	strings:
		$a = {609CE8????????8BDD5D81ED????????899D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

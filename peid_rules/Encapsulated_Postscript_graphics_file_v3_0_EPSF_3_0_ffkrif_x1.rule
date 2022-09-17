rule _Encapsulated_Postscript_graphics_file_v3_0_EPSF_3_0_ffkrif
{
	meta:
		description = "Encapsulated Postscript graphics file v3_0 EPSF_3_0"
	strings:
		$a = {252150532D41646F62652D332E3020455053462D332E30}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

rule _Microsoft_Visual_C__vx_x_xluljl
{
	meta:
		description = "Microsoft Visual C__ vx_x"
	strings:
		$a = {68????FD60BE????BF????B9????F3A48BF7BF????FC46E9CEFD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

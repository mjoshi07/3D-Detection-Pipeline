import glob
import open3d as o3d
import Detection_Pipeline as pcb


def visualization_video(input_dir):
    pcd_files = sorted(glob.glob(input_dir+"/*.pcd"))
    print(f"Number of files {len(pcd_files)}")

    viz = o3d.visualization.Visualizer()
    viz.create_window()

    for idx, file in enumerate(pcd_files):
        visuals = pcb.detection_pipeline(file, debug=False)

        for vi in visuals:
            viz.add_geometry(vi)
            viz.update_geometry(vi)
        viz.get_view_control().set_zoom(0.4)
        viz.update_renderer()
        viz.poll_events()
        # viz.capture_screen_image("temp_%04d.png" % idx)
        for vi in visuals:
            viz.remove_geometry(vi)

    viz.destroy_window()


if __name__ == "__main__":
    input_dir = "../Data/test_files/UDACITY"
    visualization_video(input_dir)
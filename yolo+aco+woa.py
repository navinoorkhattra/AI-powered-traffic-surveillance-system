from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2

model = YOLO("yolov8n.pt")

tracker = DeepSort()

cap = cv2.VideoCapture("traffic_video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detections = [(d.xyxy[0].tolist(), d.conf, d.cls) for d in results.pred[0]]
    
    tracks = tracker.update_tracks(detections, frame=frame)

    distance_matrix = np.random.rand(len(tracks), len(tracks))
    aco = AntColony(num_ants=10, num_iterations=100, decay=0.1, alpha=1, beta=2)
    optimized_paths = aco.optimize(distance_matrix)

    congestion_level = len(tracks) / frame.shape[1]
    woa = WhaleOptimization(population_size=20, max_iter=50)
    traffic_signal_time = woa.optimize(lambda x: congestion_level * np.sum(x**2), dim=1)

    cv2.imshow("Traffic Surveillance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
